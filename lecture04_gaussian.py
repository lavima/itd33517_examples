# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

image = util.img_as_float64(color.rgb2gray(io.imread(sys.argv[1])))

size = int(sys.argv[2])
if (size%2==0):
  print("Wrong size")
  sys.exit()
center = size//2

def dist(i,j):
  return (i-center,j-center) 

def gaussian():
  sigma = (size+1)/6
  mask = numpy.ndarray((size,size), dtype=numpy.float) 
  constant = 1/(2*numpy.pi*sigma**2)
  for i in range(0,size):
    for j in range(0,size):
      x,y = dist(i,j)
      mask[i,j] = constant * numpy.exp(-(x**2 + y**2)/(2*sigma**2))
  return mask

filt = gaussian()

print(filt)

out = ndimage.convolve(image, filt, mode="nearest")

io.imsave(sys.argv[3], numpy.clip(out, 0, 1))
