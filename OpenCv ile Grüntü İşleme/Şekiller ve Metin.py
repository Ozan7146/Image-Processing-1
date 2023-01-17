# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:32:32 2023

@author: ozan
Şekiller ve Metin
"""

import cv2
import numpy as np

# resim oluştur

img = np.zeros((512,512,3),np.uint8) # siyah bir resim

print(img.shape)

cv2.imshow("Siyah",img)

# çizgi ekleme
# (resim,başlangıç noktası,bitiş noktası ,renk,kalınlık)
cv2.line(img,(0,0),(512,512),(0,255,0),3) # OpenCv RGB yerine BGR kabul ediyor BGR = (0,255,0) 
cv2.imshow("Cizgi",img)

# dikdörtgen
# (resim,başlangıç noktası,bitiş noktası,renk )
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED) # Dikdörtgenin içinin dolmasını sağlıyor
cv2.imshow("Dikdortgen",img)

# Çember
# (resim,merkez,yarıçapı ,renk,içini doldur)
cv2.circle(img, (300,300),45,(0,0,255),cv2.FILLED)
cv2.imshow("Cember",img)

# metin
# (resim,başlangıç noktası,font,kalınlığı,renk)
cv2.putText(img, "Resim", (350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255)) # beyaz
cv2.imshow("Metin",img)




