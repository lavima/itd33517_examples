# imports needed for skimage and pyplot
import skimage
import numpy
import sys
from skimage import io,util,color

image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))
c = numpy.float(sys.argv[2])
gamma = numpy.float(sys.argv[3])

#height, width = image.shape
#out = numpy.zeros(image.shape, dtype=numpy.float)
#for i in range(0,height):
#  for j in range(0,width):
#    out[i,j] = c*image[i,j]**gamma

out = c*image**gamma

out = numpy.clip(out, 0, 1)

outFile = sys.argv[4]
io.imsave(outFile, out)
    

