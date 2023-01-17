# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:37:07 2023

@author: ozan7
"""

#py dosyası ile resimler aynı klasörde bulunmuyorsa resimlerin yerini belirtmemiz gerekiyor

import cv2

#içe aktarma
 
img = cv2.imread("kpk.jpg",0)

#görselleştirme
cv2.imshow("Ilk Resim",img)

#resimler 2 boyutlu matrislerdir

#klavye bağlantısı
k = cv2.waitKey(0) &0xFF

# k == 27 esc tuşunun karşılığı
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("dog1.png",img) # (kaydedilen yeni resmin adı,kaydedeceğimiz resim)
    cv2.destroyAllWindows()
