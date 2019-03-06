# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,color,exposure,io
from scipy import fftpack

# Read image, convert to gray, convert to float
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Read in cutoff constant
cutoff = float(sys.argv[2])

# Read in width constant
band_width = float(sys.argv[3])

# Retrieve the image dimensions
height,width = image.shape

# Find the dimensions of the padded image
padded_height = 2*height
padded_width = 2*width

# Create the padded image
padded = numpy.zeros((padded_height,padded_width))
padded[0:height,0:width] = image

# Create an image to store the center-transformed (frequency) image
image_trans = numpy.zeros(padded.shape)

# Transform each pixel in the image by multiplying with -1**(i+j) (see 
# slides/book) to translate the fourier transformed image to height/2 width/2 
# i.e. the center of the image
for i in range(padded_height):
  for j in range(padded_width):
    image_trans[i,j] = padded[i,j]*((-1)**(i+j))

# Perform the fourier transformation
fourier_transformed = fftpack.fft2(image_trans)

# A function for calculating the center-aligned distance squared. This function can be
# used to create any center-aligned filter.
def dist2(i,j):
  center_i, center_j = (padded_height//2, padded_width//2)
  return ((i-center_i)**2 + (j-center_j)**2) 
 
# A function for calculating distance
def dist(i,j):
  return dist2(i,j)**0.5 
 
# Create a Gaussian low pass filter
filt = numpy.zeros(padded.shape)
for i in range(padded_height):
  for j in range(padded_width):
    filt[i,j] = 1 - numpy.exp(-((dist2(i,j)-cutoff**2)/(max(dist(i,j),1)*band_width))**2) 

# Save filter for debug purposes
io.imsave("gaussian_band_reject_filter.png", filt)

# Perform the filtering 
filtered = filt*fourier_transformed

# Transform back to spatial domain
filtered_image = fftpack.ifft2(filtered)

# Translate back to top-left alignment (reverse the tranlation)
filtered_translated = numpy.zeros(padded.shape)
for i in range(padded_height):
  for j in range(padded_width):
    filtered_translated[i,j] = filtered_image[i,j]*((-1)**(i+j))

# Retrieve the sub-image corresponding to the original image
filtered_cropped = filtered_translated[0:height,0:width]

# Save the clipped result
io.imsave(sys.argv[4],numpy.clip(filtered_cropped,0,1))
