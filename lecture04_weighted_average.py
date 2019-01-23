# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color

image = util.img_as_float64(color.rgb2gray(io.imread(sys.argv[1])))

size = 3

filt = numpy.ndarray([[1,2,1],[2,4,2],[1,2,1]], dtype=numpy.float)
filt = filt / numpy.sum(filt) 

print(filt)

out = scipy.ndimage.convolve(image, filt, mode="constant", cval=0)

io.imsave(sys.argv[3], numpy.clip(out, 0, 1))
