# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,io

# Read in image and convert it to boolean
image = util.img_as_bool(io.imread(sys.argv[1]))

# Read in the structuring element (SE) and convert it to boolean
se = util.img_as_bool(io.imread(sys.argv[2]))

# Get the height and width of the SE
se_height,se_width = se.shape

# Find the center indices
pad_v = se_height//2
pad_h = se_width//2

# Pad the input image with numpy.util.pad 
padded = util.pad(image,(pad_v,pad_h),mode="constant")

# Create output image
out = numpy.zeros(image.shape,dtype=bool)

# Loop through the image (follow image indices)
for i in range(image.shape[0]):
  for j in range(image.shape[1]):
    # Retrieve subimage from padded image (not index-aligned with the image)
    subimage = padded[i:i+se_height,j:j+se_width]
    # Determine whether or not we have an overlap at the current position
    out[i,j] = numpy.array_equal(subimage*se,se)

# Save output image
io.imsave(sys.argv[3],util.img_as_ubyte(out))
