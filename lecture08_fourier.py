# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,color,exposure,io
from scipy import fftpack

# Read image, convert to gray, convert to float
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Retrieve the image dimensions
height,width = image.shape

# Create an image to store the transformed image
image_trans = numpy.zeros(image.shape)
# Transform each pixel in the image by multiplying with -1**(i+j) (see 
# slides/book) to translate the fourier transformed image to height/2 width/2 
# i.e. the center of the image
for i in range(height):
  for j in range(width):
    image_trans[i,j] = image[i,j]*((-1)**(i+j))

# Perform the fourier transformation
ft = fftpack.fft2(image_trans)

# Get the fourier spectrum by finding the length of the complex number vectors
ft = numpy.absolute(ft)

# Log transformation (see own lecture)
out = numpy.zeros(image.shape)
for i in range(0, image.shape[0]):
  for j in range(0, image.shape[1]):
    out[i,j] = numpy.log(1+ft[i,j])

# Save the rescaled result
io.imsave(sys.argv[2],exposure.rescale_intensity(out))
