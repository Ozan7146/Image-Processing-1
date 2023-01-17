# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 21:14:19 2023

@author: ozan
kamera açma ve video kaydı
"""
import cv2

#capture
cap = cv2.VideoCapture(0) #2 kamera varsa 1 veya 0 yaz

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

print(width,height)

# video kaydet
writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))
# fourcc windowsta çerçeveleri sıkıştırmak için kullanılan codec kodu 20=frame per second,en video kaydedicimizin boyutu 640 640 
# ilki dosya ismi
while True:
    
    ret,frame = cap.read()
    cv2.imshow("Video",frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    # video kaydını durdurmak için
cap.release()
writer.release() #writer'a yazma işlemim bitti
cv2.destroyAllWindows()
        


