# imports needed for skimage
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read in image and convert to appropriate format
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

sobel_x = numpy.asarray([[-1,0,1],[-2, 0, 2],[-1,0,1]])
sobel_y = numpy.asarray([[-1,-2,-1],[0, 0, 0],[1,2,1]])

grad_x = ndimage.convolve(image, sobel_x, mode="nearest")
grad_y = ndimage.convolve(image, sobel_y, mode="nearest")

out = numpy.sqrt(grad_x**2 + grad_y**2)

io.imsave(sys.argv[2], numpy.clip(out,0,1))
