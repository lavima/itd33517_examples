# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color

image = util.img_as_float64(color.rgb2gray(io.imread(sys.argv[1])))

size = int(sys.argv[2])
center = size/2

def dist((i,j)):
  (i-center,j-center) 

def gaussian():
  mask = numpy.ndarray((size,size), dtype=numpy.float) 
  for i in range(0,size):
    for j in range(0,size):
      (s,t) = dist(i,j)
      #mask[i,j] = equation

print(filt)

out = scipy.ndimage.convolve(image, filt, mode="constant", cval=0)

io.imsave(sys.argv[3], numpy.clip(out, 0, 1))
