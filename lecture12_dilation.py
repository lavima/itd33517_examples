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

se_rotated = numpy.rot90(se,2)

# Loop through the image (follow image indices)
for i in range(image.shape[0]):
  for j in range(image.shape[1]):
    # Retrieve subimage from padded image (not index-aligned with the image)
    subimage = padded[i:i+se_height,j:j+se_width]

    out[i,j] = numpy.max(numpy.ubyte(subimage*se_rotated)) 

# Save output image
io.imsave(sys.argv[3],util.img_as_ubyte(out))
