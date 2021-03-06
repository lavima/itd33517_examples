# imports needed for skimage and pyplot
import skimage
import numpy
from skimage import io,util

# Read in the image we want to work with and convert it to floats
image = util.img_as_float(io.imread("M101.jpg"))

# How many noisy images will we generate? 
num_images = 100

# Generate noisy images in a list. You might need more than 100 images to be 
# to remove noise with 0.02 variance, but memory demand will quickly become an 
# issue. 
noised_images = []
for i in range(0, num_images):
  noised_images.append(util.random_noise(image, mode="gaussian", seed=i, var=0.02, clip=False))

# Add together all the images and divide by the number of noisy images
average = sum(noised_images)/num_images

# Save the result. Note that we clip the resulting values at 0 and 1 
io.imsave("M101_averaged.png", numpy.clip(average,0.0,1.0))


