# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read image and convert it to grayscale and float
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Create filter by specifying the values directly and normalizing 
filt = numpy.asarray([[1,2,1],[2,4,2],[1,2,1]], dtype=numpy.float)
filt = filt / numpy.sum(filt) 

# Show filter
print(filt)

# Perform the smoothing 
out = scipy.ndimage.convolve(image, filt, mode="constant", cval=0)

# Save the result
io.imsave(sys.argv[2], numpy.clip(out, 0, 1))
