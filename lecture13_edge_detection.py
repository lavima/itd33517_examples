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
filt = gaussian()

smooth = ndimage.convolve(image, filt, mode="nearest")

# Create the two filter maskis
sobel_x = numpy.asarray([[-1,0,1],[-2, 0, 2],[-1,0,1]])
sobel_y = numpy.asarray([[-1,-2,-1],[0, 0, 0],[1,2,1]])

# Concolve the image with both filters
grad_x = ndimage.convolve(smooth, sobel_x, mode="nearest")
grad_y = ndimage.convolve(smooth, sobel_y, mode="nearest")

# Find the length of the vector made up of the two images
grad = (grad_x**2 + grad_y**2)**0.5

# Thresholding 
threshold = float(sys.argv[3])
binary = grad > threshold


io.imsave(sys.argv[4], util.img_as_ubyte(binary))
