# imports needed for skimage
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read in image and convert to appropriate format
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Read in the sharpening constant from command line
c = float(sys.argv[2])

# Create the Laplacian filter mask. This version of the filter generates positive 
# values for brighter values. The negated alternative generates negative values for
# brighter values. 
mask = numpy.asarray([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

# Filter the image with the filter
laplacian = ndimage.convolve(image, mask, mode="nearest")

# Perform the sharpening as specified. If the negated filter is used, one must 
# subtract instead of add
out = image + c*laplacian

# Save the clipped result
io.imsave(sys.argv[3], numpy.clip(out,0,1))


