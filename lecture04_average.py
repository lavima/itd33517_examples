# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read image and convert it to grayscale and float
image = util.img_as_float64(color.rgb2gray(io.imread(sys.argv[1])))

# Read in the size of the filter and validate the value to be odd
size = int(sys.argv[2])
if (size%2==0):
  print("Wrong size")
  sys.exit()

# Create the filter with the specified size
filt = numpy.ones((size, size))
# Normalize the values in the filter
#filt = filt / numpy.sum(filt)
filt = filt / size**2 

# Show filter
print(filt)

# Perform the smoothing 
out = ndimage.convolve(image, filt, mode="constant", cval=0)

# Save the result
io.imsave(sys.argv[3], numpy.clip(out, 0, 1))
