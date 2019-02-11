import skimage
import scipy
import sys
import numpy
from skimage import util,color,exposure,io
from scipy import fftpack

image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

height,width = image.shape

image_trans = numpy.zeros(image.shape)

for i in range(height):
  for j in range(width):
    image_trans[i,j] = image[i,j]*((-1)**(i+j))

ft = fftpack.fft2(image_trans)

ft = numpy.absolute(ft)

out = numpy.zeros(image.shape)
for i in range(0, image.shape[0]):
  for j in range(0, image.shape[1]):
    out[i,j] = numpy.log(1+ft[i,j])


io.imsave(sys.argv[2],exposure.rescale_intensity(out))
