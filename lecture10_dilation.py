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

    # Add code to rotate the SE

    # Determine whether we have an overlap
    out[i,j] = numpy.sum(subimage*se)>0

# Save output image
io.imsave(sys.argv[3],util.img_as_ubyte(out))
