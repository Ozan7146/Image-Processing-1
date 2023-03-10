# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 13:34:36 2023

@author: ozan
Renkleri ayırmak veana hatları netleştirmek için
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img,cmap = "gray") #siyah beyaz için
plt.axis("off")
plt.show()


# eşikleme (ana hat belirleme)
# thres = 60 üzerindekileri beyaz yapıyor
_,thresh_img = cv2.threshold(img,thresh = 60,maxval = 255,type = cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img,cmap = "gray") #siyah beyaz için
plt.axis("off")
plt.show()

#uyarlamalı eşik değeri

thresh_img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8,)
plt.figure()
plt.imshow(thresh_img2,cmap = "gray") #siyah beyaz için
plt.axis("off")
plt.show()





