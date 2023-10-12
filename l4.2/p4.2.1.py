from skimage.io import imshow,imsave,imread
from matplotlib import pyplot as plt
import numpy as np
img = imread("https://stepik.org/media/attachments/lesson/61041/tiger-gray-small.png")
out_img = np.array(img)
for i in range(3,len(img)-3):
    for j in range(3,len(img[0])-3):
            temp = img[i-3:i+4,j-3:j+4]
            m = np.median(temp)
            out_img[i][j] = m
out_img = out_img[3:len(img)-3,3:len(img[0])-3]
imshow(out_img)
plt.show()