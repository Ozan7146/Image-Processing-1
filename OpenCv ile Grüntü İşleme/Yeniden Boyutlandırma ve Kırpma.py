# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:13:27 2023

@author: ozan
yeniden boyutlandır ve kırp
"""

import cv2

img = cv2.imread("img1.jpg",0)
cv2.namedWindow("Orijinal",cv2.WINDOW_NORMAL)
print("Resim Boyutu:", img.shape)  #(911,1368)
cv2.imshow("Orijinal", img)



# resize
imgResized = cv2.resize(img, (10000,10000))

print("Resized Img Shape: ", imgResized.shape)
cv2.namedWindow("Image Resized",cv2.WINDOW_NORMAL)
cv2.imshow("Image Resized",imgResized)


# kırp
imgCropped = img[:2000,0:3000] # 0 dan başlayıp x eksende 200 pikseli alıyoruz,y ekseninde de 0 dan 300 e kadar olan pikselleri alıyoruz
#cv2.namedWindow("Kirpik Resim:",cv2.WINDOW_NORMAL)
cv2.imshow("Kirpik Resim:",imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
