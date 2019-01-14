# imports needed for skimage and pyplot
import skimage
import numpy
from skimage import io,util

# Read in the image we want to work with
image = io.imread("M101.jpg")

# How many noisy images will we generate? 
num_images = 100

# Generate noisy images in a list
noised_images = []
for i in range(0, num_images):
  noised_images.append(util.random_noise(image, mode="gaussian", var=0.1, clip=False))

# Add together all the images and divide by the number of noisy images
average = sum(noised_images)/num_images

# Save the result. Note that we clip the resulting values at 0 and 1 
io.imsave("M101_averaged.png", numpy.clip(average,0.0,1.0))


