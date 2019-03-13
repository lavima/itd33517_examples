# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,io,morphology

# Read in image and structuring element and convert them to bool
image = util.img_as_bool(io.imread(sys.argv[1]))

padded = util.pad(image, (1,1), mode="constant")
print(padded)

# Create structuring element.
se = numpy.ones((3,3),dtype=numpy.bool) 


# skimage.morphology.binary_erosion
eroded = morphology.binary_erosion(padded,se)
print(eroded)
out = padded ^ eroded

# Save output
cropped = out[1:image.shape[0]+1,1:image.shape[1]+1]
io.imsave(sys.argv[2], util.img_as_ubyte(cropped))

