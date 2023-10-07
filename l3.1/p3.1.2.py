from skimage.io import imread, imsave, imshow
from skimage import img_as_float
from matplotlib import pyplot as plt
import numpy as np
img = imread("https://stepik.org/media/attachments/lesson/58402/tiger-low-contrast.png")
img1 = img_as_float(img)
k = round(len(img)*len(img[0])*0.05)
l = []
for i in range(len(img1)):
    for j in range(len(img1[0])):
        l.append(img1[i,j])
l.sort()
l_stripped = l[k:len(l)-1-k]
mi = l_stripped[0]
ma = l_stripped[-1]
print(ma,mi)
img_c = (img1 - mi)*(255/(ma-mi))
im_o = np.clip(img_c,0,255)
im_out = im_o.astype('uint8')
imshow(im_out)

plt.show()