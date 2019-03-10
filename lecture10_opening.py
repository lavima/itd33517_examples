# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,io,morphology

image = util.img_as_bool(io.imread(sys.argv[1]))
se = util.img_as_bool(io.imread(sys.argv[2]))

eroded = morphology.binary_erosion(image,selem=se)

opened = morphology.binary_dilation(eroded,selem=se)

io.imsave(sys.argv[3],util.img_as_ubyte(opened))

