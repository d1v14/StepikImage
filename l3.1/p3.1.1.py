from skimage.io import imread, imsave, imshow
from skimage import img_as_float
from matplotlib import pyplot as plt
import numpy as np
img = imread("https://stepik.org/media/attachments/lesson/58402/tiger-low-contrast.png")
print(img[0,0])
img1 = img_as_float(img)
print(img1[0,0])
img1 = (img - img.min()) * 255.0/(img.max()-img.min())
img1 = img1.astype('uint8')
print(img1[0,0])
imshow(img1)
plt.show()
