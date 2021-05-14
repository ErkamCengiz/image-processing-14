import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('messi.jpg',0)#gri tonlama aldık
kenarlar=cv2.Canny(resim,100,200)


plt.subplot(121),plt.imshow(resim,cmap='gray')#subplot 1 satır 2 stun 1 yere koy demek ordaki 121
plt.title('orjinal'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(kenarlar,cmap='gray')
plt.title('kenarlar'),plt.xticks([]),plt.yticks([])
plt.show()
