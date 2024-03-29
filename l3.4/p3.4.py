from skimage.io import imread,imshow,imsave
from matplotlib import pyplot as plt
import numpy as np
img = imread("l3.4/img.png")
img_o = np.array(img)
mi = 0
a,_= np.histogram(img.ravel(),bins=range(257))
for i in range(len(a)):
    if(mi!=0):
        break
    else:
        mi+=a[i]
for i in range(len(img)):
    for j in range(len(img[0])):
        img_o[i,j] = np.round((a[:img[i,j]+1].sum()-mi)/(img.shape[0]*img.shape[1]-1)*255)
imshow(img_o)
plt.show()