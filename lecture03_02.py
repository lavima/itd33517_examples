# imports needed for skimage and pyplot
import skimage
import numpy
import sys
from skimage import io,util,color

image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))
num_levels = numpy.int(sys.argv[2])

histogram = numpy.zeros((num_levels, 1), dtype=numpy.uint)

height, width = image.shape
for i in range(0,height):
  for j in range(0,width):
    histogram[int(round(image[i,j]*(num_levels-1)))] += 1 


print(histogram)
