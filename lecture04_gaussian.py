# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read in image and convert to appropriate format
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Read in the size of the mask to use, and make sure it is an odd number
size = int(sys.argv[2])
if (size%2==0):
  print("Wrong size")
  sys.exit()

# A function for converting top-left aligned coordinates to center aligned 
# coordinates
def dist(i,j):
  # Find the center index
  center = size//2
  # Return the converted coordinates
  return (i-center,j-center) 

# A function for creating a Gaussian smoothing filter
def gaussian():
  # Find the sigma to use based on the size of the filter. The sigma controls 
  # the magnitude of the values in the generated filter. The relationship 
  # between size and sigma make sure that we don't clip the lower values of the
  # bell curve.
  sigma = (size+1)/6
  
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

# Print the filter for debug purposes
print(filt)

# Smooth the image using built-in convolution operator and our filter
out = ndimage.convolve(image, filt, mode="nearest")

# Save the clipped result
io.imsave(sys.argv[3], numpy.clip(out, 0, 1))
