# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color

image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

size = int(sys.argv[2])
if (size%2==0):
  print("Wrong size")
  sys.exit()

filt = numpy.ones((size, size))
#filt = filt / numpy.sum(filt)
filt = filt / size**2 

print(filt)

out = scipy.ndimage.filters.convolve(image, filt, mode="constant", cval=0)
