# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read in image and convert to appropriate format
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Read the sigma to use in the gaussian noise reduction filter from the second 
# command line argument
sigma = float(sys.argv[2])

# Read in the boos factor k (see lecture notes or book)
k = float(sys.argv[3])

# The following is a direct copy from the gaussian noise reduction code in
# lecture04_guassian_alt.py

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

# Smooth the image using built-in convolution operator and our filter
smooth = ndimage.convolve(image, filt, mode="nearest")

# End of copy / Start of highboost filtering

# Find the highboost_mask. Note that in this case, the term mask does not refer
# to a filter mask, but a highboost mask. The highboost mask has the same size
# as the image
highboost_mask = image - smooth

# Perform the highboost filtering
highboost = image + k*highboost_mask

# Save te clipped result
io.imsave(sys.argv[4], numpy.clip(highboost,0,1)) 
