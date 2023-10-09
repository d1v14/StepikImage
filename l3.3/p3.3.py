from skimage.io import imread,imshow
from skimage import img_as_float, img_as_ubyte
from matplotlib import pyplot as plt
import numpy as np
img = imread("https://stepik.org/media/attachments/lesson/60610/railroad.png")
img_f = img_as_float(img)
avgR = img_f[:,:,0].sum()/(len(img)*len(img[0]))
avgG = img_f[:,:,1].sum()/(len(img)*len(img[0]))
avgB = img_f[:,:,2].sum()/(len(img)*len(img[0]))
avg = (avgR+avgB+avgG)/3
rw = avgR/avg
gw = avgG/avg
bw = avgB/avg
r = img_f[:,:,0]
g = img_f[:,:,1]
b = img_f[:,:,2]
r /= rw
b /= bw
g /= gw
res = np.dstack((r,g,b))
res1 = np.clip(res,0,1)
imshow(res1)
plt.show()