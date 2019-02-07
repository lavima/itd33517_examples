# imports needed for skimage
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

# Get the size of the image
height, width = image.shape

# Find the center index in the window. Note that we are not using a filter mask
# and the convolution operator. Instead we are using a sliding window with logic
center = size//2

# Create the output image to store the result
out = numpy.zeros(image.shape, dtype=numpy.float)

# Loop through the image in row-major fashion
for i in range(0,height):
  for j in range(0,width):
    # Fetch the subimage. max and min are used instead of a series of if else 
    # statements. This pattern can be used in other circumstances as well.
    subimage = image[max(i-center,0):min(i+center+1,height),max(j-center,0):min(j+center+1,width)]
    # Flatten the image i.e. convert into a one-dimensional array
    flat = subimage.flatten() 
    # Sort the flattened subimage
    sort = numpy.sort(flat)
    # Store the middle value in the output
    out[i,j] = sort[len(sort)//2] 
  
# Save the output image
io.imsave(sys.argv[3], out)
