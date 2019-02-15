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

# A function for converting left aligned coordinates to center aligned 
# coordinates
def dist(i):
  # Find the center index
  center = size//2
  # Return the converted coordinates
  return i-center 

# A function for creating a Gaussian smoothing filter
def gaussian():
  # Create the filter image
  mask = numpy.ndarray((size,1), dtype=numpy.float) 

  # Calculate the constant factor of the Gaussian equation. Not needed if we
  # are normalizing the filter after calculations
  constant = 1/(2*numpy.pi*sigma**2)**0.5
   
  # Loop through all the pixels of the mask
  for i in range(0,size):
    # Find the center-aligned coordinates for the current pixel
    x = dist(i)
    # Calculate the pixel value 
    mask[i,0] = constant * numpy.exp(-(x**2)/(2*sigma**2))

  return mask

# Create the Gaussian filter
filt = gaussian()

# Print the filter for debug purposes
print(filt)
print(numpy.sum(filt))

# Smooth the image using built-in convolution operator and our filter. Note that we convole 
# times, first with the vertical filter, then with the horizontal filter.
filtered = ndimage.convolve(image, filt, mode="nearest")
out = ndimage.convolve(filtered, numpy.transpose(filt), mode="nearest")

# Save the clipped result
io.imsave(sys.argv[3], numpy.clip(out, 0, 1))
