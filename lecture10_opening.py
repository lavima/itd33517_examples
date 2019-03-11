# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,io,morphology

# Read in image and structuring element and convert them to bool
image = util.img_as_bool(io.imread(sys.argv[1]))
se = util.img_as_bool(io.imread(sys.argv[2]))

# Erode the input image with the SE using skimage.morphology.binary_erosion
eroded = morphology.binary_erosion(image,selem=se)

# Dilate the input image with the SE using skimage.morphology.binary_dilation
opened = morphology.binary_dilation(eroded,selem=se)

# Save the opened image 
io.imsave(sys.argv[3],util.img_as_ubyte(opened))

