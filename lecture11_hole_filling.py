# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,io,morphology

image = util.img_as_bool(io.imread(sys.argv[1]))
print(image)

image_iter = numpy.zeros(image.shape, dtype=bool)
image_iter[258,148] = True


se = numpy.ones((3,3),dtype=bool)

image_neg = ~image  

while True:
  image_iter2 = morphology.binary_dilation(image_iter,se) & image_neg
  if numpy.array_equal(image_iter2, image_iter):
    break
  image_iter = image_iter2

out = image_iter|image

io.imsave(sys.argv[2], util.img_as_ubyte(out))
