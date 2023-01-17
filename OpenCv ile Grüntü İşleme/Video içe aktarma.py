# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 23:09:37 2023

@author: ozan7
"""

import cv2
import time

# video ismi
video_name = "vid.mp4"

# video içe aktar: capture cap
cap = cv2.VideoCapture(video_name)

print("Genişlik: ",cap.get(3))
print("Yükseklik: ",cap.get(4))


# videonun açılıp açılmadığını anlamak için yaptık.
if cap.isOpened() == False:
    print("Hata")

while True:   #döngüye almazsak video yerine resim olur 
    # videoyu okumak
    # return = ret = true? veya false? verecek. frame de frame'i verecek.
    ret, frame = cap.read()
    
    # okuyabildiyse içeri girsin
    if ret == True:
        time.sleep(0.01) # uyarı: kullanmazsak video çok hızlı hareket eder 
        cv2.imshow("Video",frame)
    
    else: break # video bitince kendisi çıkması için

    if cv2.waitKey(1) &0xFF == ord("q"): # videodan kendi isteğimizle çıkmak için
        break

# stop capture
cap.release()
cv2.destroyAllWindows()






