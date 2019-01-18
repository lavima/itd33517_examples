# Imports needed for skimage and pyplot
import skimage
import numpy
import sys
from skimage import io,util,color

# Import image using the first command line argument. The image is converted to 
# grayscale before type conversion to float
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))
# The number of levels to use for the histogram
num_levels = numpy.int(sys.argv[2])

# Create an numpy.ndarray for our histogram. We could also use a list, but 
# arrays have more efficient operations
histogram = numpy.zeros((num_levels, 1), dtype=numpy.uint)

# Loop through all the pixels in the image
height, width = image.shape
for i in range(0,height):
  for j in range(0,width):
    # All values will be truncated towards zero (decimals removed), which will 
    # make the last bin to collect only the extreme value 1
    #bin_index = int(image[i,j]*(num_levels-1))

    # This solution fixes this issue by rounding the values before truncing 
    # them. This will make all the bins the same size, expect for the first and
    # last, which are half the size of the other bins
    # bin_index = int(round(image[i,j]*(num_levels-1)))

    # This solution treats the extreme value of 1 as a special case. This
    # solution has roughly equal sized bins.
    bin_index = int(min(image[i,j]*num_levels, num_levels-1))

    # Increase the count of the bin
    histogram[bin_index] += 1 

print(histogram)
