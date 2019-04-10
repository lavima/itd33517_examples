# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read in image and convert to appropriate format
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Read in sigma 
sigma = float(sys.argv[2])

# Calculate size of filter mask
size = int(6*sigma)-1

# A function for converting top-left aligned coordinates to center aligned 
# coordinates
def dist(i,j):
  # Find the center index
  center = size//2
  # Return the converted coordinates
  return (i-center,j-center) 

# A function for creating a Gaussian smoothing filter
def gaussian():
  # Create the filter image
  mask = numpy.ndarray((size,size), dtype=numpy.float) 

  # Calculate the constant factor of the Gaussian equation. Not needed if we
  # are normalizing the filter after calculations
  constant = 1/(2*numpy.pi*sigma**2)
   
  # Loop through all the pixels of the mask
  for i in range(0,size):
    for j in range(0,size):
      # Find the center-aligned coordinates for the current pixel
      x,y = dist(i,j)
      # Calculate the pixel value 
      mask[i,j] = constant * numpy.exp(-(x**2 + y**2)/(2*sigma**2))

  return mask

# Create the Gaussian filter
gaussian_filter = gaussian()

# Convolve with gaussian filter to remove noise
smooth = ndimage.convolve(image, gaussian_filter, mode="nearest")

# Create and convolve with laplacian filter to remove noise
laplacian_filter = numpy.asarray([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

laplacian = ndimage.convolve(smooth, laplacian_filter, mode="nearest")

zero_crossed = numpy.zeros(image.shape,dtype=numpy.float)
height, width = image.shape
for i in range(1,height-1):
  for j in range(1,width-1):
    subimage = laplacian[i-1:i+2,j-1:j+2]  
    if subimage[0,0]*subimage[2,2]<0:
      zero_crossed[i,j] = abs(subimage[0,0]-subimage[2,2])
    elif subimage[0,1]*subimage[2,1]<0:
      zero_crossed[i,j] = abs(subimage[0,1]-subimage[2,1])
    elif subimage[0,2]*subimage[2,0]<0:
      zero_crossed[i,j] = abs(subimage[0,2]-subimage[2,0])
    elif subimage[1,0]*subimage[1,2]<0:
      zero_crossed[i,j] = abs(subimage[1,0]-subimage[1,2])

out = zero_crossed > float(sys.argv[3])
io.imsave(sys.argv[4], util.img_as_ubyte(out))
