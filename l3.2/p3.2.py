from skimage.io import imread,imshow
from skimage import img_as_float, img_as_ubyte
from matplotlib import pyplot as plt
import numpy as np
img = imread("l3.2/tiger-color.png")
img_f = img_as_float(img)
img_yuv = np.array(img_f)

img_y =  0.2126*img_f[:, :, 0] + 0.7152*img_f[:, :, 1] + 0.0722*img_f[:, :, 2]
img_u = -0.0999*img_f[:, :, 0] - 0.3360*img_f[:, :, 1] + 0.4360*img_f[:, :, 2]
img_v =  0.6150*img_f[:, :, 0] - 0.5586*img_f[:, :, 1] - 0.0563*img_f[:, :, 2]

im  = np.array(img_y).reshape(len(img_y)*len(img_y[0]))
im.sort()
a,b,c = plt.hist(im,bins =257)
k = round(len(im)*0.05)
im_stripped = im[k:-k-1]
mi = im_stripped[0]
ma = im_stripped[-1]

img_y = (img_y - mi)/(ma-mi)
img_y_clipped = np.clip(img_y,0,1)
img_r = img_y + 1.2803 * img_v
img_g = img_y - 0.2148 * img_u - 0.3805*img_v
img_b = img_y + 2.1227 * img_u
res = np.dstack((img_r,img_g,img_b))
res = np.clip(res,0,1)
res = img_as_ubyte(res)
imshow(res)
# a,b,c = plt.hist(img_yuv[:,:,0].ravel(),bins = 257)

# img_yuv[:,:,0] = (img_yuv[:,:,0] - l_stripped[0])/(l_stripped[-1]-l_stripped[0])
# a,b,c = plt.hist(img_yuv[:,:,0].ravel(),bins = 257)

#imshow(img)
plt.show()