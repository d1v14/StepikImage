from skimage.io import imsave, imread, imshow
from matplotlib import pyplot as plt
from numpy import dstack
import numpy as np
from skimage import img_as_float
img = imread("l2.3/img.png")
sizey = len(img)//3
sizex = len(img[0])
b = img[:sizey,:]
g = img[sizey:sizey*2,:]
r = img[sizey*2+1:sizey*3+1,:]

cuty = int(sizey*0.1)
cutx = int(sizex*0.1)
b_trimmed = img_as_float(b[cuty:sizey-cuty,cutx:sizex-cutx])
g_trimmed = img_as_float(g[cuty:sizey-cuty,cutx: sizex-cutx])
r_trimmed = img_as_float(r[cuty:sizey-cuty,cutx: sizex-cutx])
correlationb = 0
correlationr = 0
x = 0 
y = 0
xr = 0 
yr = 0
for i  in range(-15,16):
    for j in range(-15,16):
        test = np.roll(b_trimmed,i,0)
        test = np.roll(test,j,1)
        if  (g_trimmed*test).sum() > correlationb:
            correlationb = (g_trimmed*test).sum() 
            y = j
            x = i

for i  in range(-15,16):
    for j in range(-15,16):
        test = np.roll(r_trimmed,i,0)
        test = np.roll(test,j,1)
        if  (g_trimmed*test).sum() > correlationr:
            correlationr = (g_trimmed*test).sum() 
            yr = j
            xr = i

testb = np.roll(b_trimmed,x,0)
testb = np.roll(testb,y,1)
testr = np.roll(r_trimmed,xr,0)
testr = np.roll(testr,yr,1)
print()
imshow(dstack((testr,g_trimmed,testb)))
plt.show()