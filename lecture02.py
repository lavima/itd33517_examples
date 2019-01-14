# imports needed for skimage and pyplot
import skimage
import numpy
from skimage import io,util

image = io.imread("M101.jpg")

num_images = 100

noised_images = []
for i in range(0, num_images):
  noised_images.append(util.random_noise(image, mode="gaussian", var=0.1, clip=False))

average = sum(noised_images)/num_images

io.imsave("M101_averaged.png", numpy.clip(average,0.0,1.0))


