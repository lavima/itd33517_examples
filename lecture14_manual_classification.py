import skimage
import numpy
import sys
import scipy
from skimage import io,util,color
from scipy import ndimage

if len(sys.argv)>1:
  image = util.img_as_bool(color.rgb2gray(io.imread(sys.argv[1])))
  images = [image]
else:
  image1 = util.img_as_bool(color.rgb2gray(io.imread("o1_1.png")))
  image2 = util.img_as_bool(color.rgb2gray(io.imread("o1_2.png")))
  image3 = util.img_as_bool(color.rgb2gray(io.imread("o2_1.png")))
  image4 = util.img_as_bool(color.rgb2gray(io.imread("o3_1.png")))
  image5 = util.img_as_bool(color.rgb2gray(io.imread("o3_2.png")))
  image6 = util.img_as_bool(color.rgb2gray(io.imread("o3_3.png")))
  image7 = util.img_as_bool(color.rgb2gray(io.imread("o4_1.png")))
  image8 = util.img_as_bool(color.rgb2gray(io.imread("o4_2.png")))

  images = [image1,image2,image3,image4,image5,image6,image7,image8]

def area(image):
  return numpy.sum(image)
 
def circumference(image):
  se = numpy.ones((3,3),dtype=bool)
  eroded = ndimage.binary_erosion(image,se)
  return numpy.sum(image^eroded)

def opened_area(image):
  se = numpy.ones((3,3),dtype=bool)
  opened = ndimage.binary_opening(image,se)
  return numpy.sum(opened)
 

for image in images:
  a = area(image)
  c = circumference(image)
  oa = opened_area(image)
  # Classify
  if a<25 and c<25:
    print("Object 1")
  elif a>25 and c>25:
    print("Object 2")
  elif a>25 and c<25 and oa<26:
    print("Object 3")
  elif a>25 and c<25 and oa>26:
    print("Object 4")
