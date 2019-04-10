import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

image1 = util.img_as_bool(color.rgb2gray(io.imread(sys.argv[1])))

def area(image):
  return numpy.sum(image)
 
def circumference(image):
  se = numpy.ones((3,3),dtype=bool)
  eroded = ndimage.binary_erosion(image1,se)
  return numpy.sum(image^eroded)

print(area(image1))
print(circumference(image1))
