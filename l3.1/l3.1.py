from skimage.io import imread, imsave, imshow
from matplotlib import pyplot as plt
import numpy as np
img = imread("https://stepik.org/media/attachments/lesson/58181/tiger-color.png")
value, bin_edges,patches  =plt.hist(img.ravel(),bins = range(257)) #Строит гистограмму по изображению
plt.show()                                                         #Для построения гистограммы нужно вытянуть изображение в         одномерный массив с помощью функции ravel() и задать длину оси х с помощью bins гистограмма так же возвращает значения.

