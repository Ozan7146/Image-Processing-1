# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:48:56 2023

@author: ozan
Görüntülerin Birleştirilmesi
"""


import cv2
import numpy as np

# resmi içe aktarma
img = cv2.imread("Elon.png")
cv2.imshow("Orijinal",img)

# yatay birleştirme
hor = np.hstack((img,img))
cv2.imshow("Horizontal:",hor)

# dikey birleştirme
ver = np.vstack((img,img))
cv2.imshow("Vertical:",ver)





















