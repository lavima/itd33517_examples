# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,io,color

# Read in image and convert it to boolean
image = util.img_as_ubyte(color.rgb2gray(io.imread(sys.argv[1])))

# Read in the structuring element (SE) and convert it to boolean
se = util.img_as_float(color.rgb2gray(io.imread(sys.argv[2])))

# Get the height and width of the SE
se_height,se_width = se.shape

# Find the center indices
pad_v = se_height//2
pad_h = se_width//2

# Pad the input image with numpy.util.pad 
padded = util.pad(image,(pad_v,pad_h),mode="constant")

# Create output image
out = numpy.zeros(image.shape,dtype=numpy.ubyte)

# Loop through the image (follow image indices)
for i in range(image.shape[0]):
  for j in range(image.shape[1]):
    # Retrieve subimage from padded image (not index-aligned with the image)
    subimage = padded[i:i+se_height,j:j+se_width]
    # Create a mask that is white where the SE is zero. 
    se_mask = util.img_as_ubyte(se==0.0)
    # Multiply the subimage with the se to get the overlapping values, then add the mask
    # to make sure that values outside the overlapping values are larger than the ones within. 
    # Get the output value by finding the smallest value in the result from these operations.
    out[i,j] = numpy.min(numpy.ubyte(subimage*se)+se_mask)

# Save output image
io.imsave(sys.argv[3],util.img_as_ubyte(out))
