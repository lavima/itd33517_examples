# Our imports
import skimage
import scipy
import sys
import numpy
from skimage import util,io

image = util.img_as_bool(io.imread(sys.argv[1]))
se = util.img_as_bool(io.imread(sys.argv[2]))

se_height,se_width = se.shape

pad_v = se_height//2
pad_h = se_width//2

padded = util.pad(image,(pad_v,pad_h),mode="constant")

out = numpy.zeros(image.shape,dtype=bool)
for i in range(image.shape[0]):
  for j in range(image.shape[1]):
    subimage = padded[i:i+se_height,j:j+se_width]
    out[i,j] = numpy.array_equal(subimage*se,se)

io.imsave(sys.argv[3],util.img_as_ubyte(out))
