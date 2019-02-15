# imports needed for skimage
import skimage
import numpy
import sys
from skimage import io,util,color

# Read in image and convert it to grayscale and unsigned byte format
image = util.img_as_ubyte(color.rgb2gray(io.imread(sys.argv[1])))

# An image for storing the histogram: One bin for each intensity in 8-bit grayscale.
histogram = numpy.zeros((256, 1), dtype=numpy.uint)

# Collect the histogram
height, width = image.shape
for i in range(0,height):
  for j in range(0,width):
    histogram[image[i,j]] += 1 

# Convert the histogram counts to probabilities
prob = histogram / (width*height)

# Create an histogram to store the accumulated probabilities
accum = numpy.zeros(prob.shape)
accum[0,0] = prob[0,0]
for i in range(1,256):
  accum[i,0] = accum[i-1,0]+prob[i,0] 

# Create an histogram to store the accumulated probabilities
spec_accum = numpy.zeros(prob.shape)
spec_accum[0,0] = spec_prob[0,0]
for i in range(1,256):
  spec_accum[i,0] = spec_accum[i-1,0]+spec_prob[i,0] 

spec_map = numpy.ubyte(255*spec_accum)

# Create the output image. Note that we are using unsigned bytes to make sure
# that the intensities are discrete.
out = numpy.zeros(image.shape, dtype=numpy.ubyte)

# Traverse image
for i in range(0,height):
  for j in range(0,width):
    # Perform the pixel-wise transformation
    out[i,j] = numpy.ubyte(255*accum[image[i,j]])

# Save the output as is
io.imsave(sys.argv[2], out)
