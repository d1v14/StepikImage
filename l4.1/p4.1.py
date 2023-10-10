from skimage.io import imshow,imread,imsave
from matplotlib import pyplot as plt
from scipy import signal
import numpy as np
img = imread("https://stepik.org/media/attachments/lesson/61037/tiger-gray-small.png")
mask = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
img_b = signal.convolve2d(img,mask,mode="valid")
img_b = img_b / 25
img_o = img_b.astype('uint8')
imshow(img_o)
plt.show()