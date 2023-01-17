# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 01:31:41 2023

@author: ozan
Perspektif Çarpıtma
"""

import cv2
import numpy as np

img = cv2.imread("kpk.jpg")
cv2.imshow("Orijinal",img)

width = 400
height = 500

# çevirmek istediğimiz resmin köşeleri
pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])

# istediğimiz durum
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

# dönüştürlmüş resim
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Son resim",imgOutput)

