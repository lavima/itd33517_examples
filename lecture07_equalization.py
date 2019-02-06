# imports needed for skimage
import skimage
import numpy
import sys
from skimage import io,util,color

image = util.img_as_ubyte(color.rgb2gray(io.imread(sys.argv[1])))

histogram = numpy.zeros((256, 1), dtype=numpy.uint)

height, width = image.shape
for i in range(0,height):
  for j in range(0,width):
    histogram[image[i,j]] += 1 

prob = histogram / (width*height)

accum = numpy.zeros(prob.shape)
accum[0,0] = prob[0,0]
for i in range(1,256):
  accum[i,0] = accum[i-1,0]+prob[i,0] 

out = numpy.zeros(image.shape, dtype=numpy.ubyte)
for i in range(0,height):
  for j in range(0,width):
    out[i,j] = numpy.ubyte(255*accum[image[i,j]])

io.imsave(sys.argv[2], out)
