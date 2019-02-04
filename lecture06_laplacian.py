# imports needed for skimage
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read in image and convert to appropriate format
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

c = float(sys.argv[2])

mask = numpy.asarray([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

laplacian = ndimage.convolve(image, mask, mode="nearest")

out = image + c*laplacian

io.imsave(sys.argv[3], numpy.clip(out,0,1))


