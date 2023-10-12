from skimage.io import imread,imshow,imsave
from skimage import img_as_float,img_as_ubyte
from scipy import signal as sg
from matplotlib import pyplot as plt
import math
import numpy as np
def Gauss(x,y,s):
    ans = 1/(2*math.pi*pow(s,2))
    ans *= math.exp((-pow(x,2)-pow(y,2))/(2*pow(s,2)))
    return ans

img = imread("l4.1/img.png")
img_f = img_as_float(img)
s = 0.66
k=round(3*s*2+1)
arr = np.zeros((k,k),dtype = "float")
for i in range(-(k//2),(k//2)+1,1):
    for j in range(-(k//2),(k//2)+1,1):
        arr[(k//2)+i,(k//2)+j] = Gauss(i,-j,s)
d = arr.sum()

img_o = sg.convolve2d(img_f,arr,mode = "valid")
img_o = img_o / d
np.clip(img_o,0,1)
img_out = img_as_ubyte(img_o)
imshow(img_out)
plt.show()