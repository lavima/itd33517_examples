# imports needed for skimage and pyplot
import skimage
from skimage import io
from matplotlib import pyplot as plt

# Read the image called "lena.png" from file
im = io.imread("lena.png")

# Print image and image shape (dimensionality)
print(im)
print(im.shape)

# Get a subimage from im (assumes RGB image)
subim = im[10:20,10:20,:]

# Print subimage and image shape (dimensionality)
print(subim)
print(subim.shape)

# show image
io.imshow(subim)
plt.show()
