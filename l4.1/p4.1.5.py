from skimage.io import imread,imshow,imsave
from skimage import img_as_float,img_as_ubyte
from scipy import signal as sg
from matplotlib import pyplot as plt
import numpy as np

img = imread("l4.1/img.png")
ker = np.array([[-1,-2,-1],[-2,22,-2],[-1,-2,-1]])
k = 10
img_o = sg.convolve2d(img,ker,mode = "valid")
img_o = img_o / k
img_out = np.clip(img_o,0,255)
img_out = img_out.astype('uint8')
imshow(img_out)               
plt.show()
