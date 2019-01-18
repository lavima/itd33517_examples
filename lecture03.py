# imports needed for skimage and pyplot
import skimage
import numpy
import sys
from skimage import io,util,color

# Import image using the first command line argument. The image is converted to 
# grayscale before type conversion to float
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))
# The constant multiplier is read from the second command line argument
c = numpy.float(sys.argv[2])
# The gamma value is read from the third command line argument
gamma = numpy.float(sys.argv[3])

# Iterate over each pixel in the image and store the transformed values
#height, width = image.shape
#out = numpy.zeros(image.shape, dtype=numpy.float)
#for i in range(0,height):
#  for j in range(0,width):
     # This is the actual gamma transform of one pixel
#    out[i,j] = c*image[i,j]**gamma

# Vectorized version of the same as the above (preferred for runtime efficiency)
out = c*image**gamma

# Clip the values to the interval [0,1]
out = numpy.clip(out, 0, 1)

# Save the transformed image to the filename in the fourth command line argument
outFile = sys.argv[4]
io.imsave(outFile, out)
    

