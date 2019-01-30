# imports needed for skimage and pyplot
import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

# Read in image and convert to appropriate format
image = util.img_as_float(color.rgb2gray(io.imread(sys.argv[1])))

# Read in the size of the mask to use, and make sure it is an odd number
size = int(sys.argv[2])
if (size%2==0):
  print("Wrong size")
  sys.exit()

height, width = image.shape

center = size//2

out = numpy.zeros(image.shape, dtype=numpy.float)
for i in range(0,height):
  for j in range(0,width):
    subimage = image[max(i-center,0):min(i+center+1,height),max(j-center,0):min(j+center+1,width)]
    flat = subimage.flatten() 
    sort = numpy.sort(flat)
    out[i,j] = sort[len(sort)//2] 
  
io.imsave(sys.argv[3], out)
