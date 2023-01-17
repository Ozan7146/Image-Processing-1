# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:13:27 2023

@author: ozan
yeniden boyutlandır ve kırp
"""

import cv2

img = cv2.imread("Elon.png",0)
print("Resim Boyutu:", img.shape)  #(911,1368)
cv2.imshow("Orijinal", img)

# resize
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("Image Resized",imgResized)

# kırp
imgCropped = img[:200,0:300] # 0 dan başlayıp x eksende 200 pikseli alıyoruz,y ekseninde de 0 dan 300 e kadar olan pikselleri alıyoruz
cv2.imshow("Kirpik Resim:",imgCropped)
