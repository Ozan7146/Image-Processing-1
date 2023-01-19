# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 13:15:36 2023

@author: ozan
Homework 1
"""

#kütüphane import et
import cv2
import matplotlib.pyplot as plt

#içe aktar
img = cv2.imread("img1.jpg",0)
cv2.namedWindow("orijinal",cv2.WINDOW_NORMAL)
# resmi ekrana adlı olarak bas
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("orijinal",img1)

"""
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# size of the picture
print(img1.shape)
"""
#adsız resim
resized_img = cv2.resize(img1,(600,600))
cv2.imshow(resized_img)
"""

# resize
resized_img = cv2.resize(img1,(int(img.shape[1]*4/5),int(img.shape[0]*4/5)))
cv2.namedWindow("resize",cv2.WINDOW_NORMAL)
cv2.imshow("resize",resized_img)

# yazı ekleme
x = cv2.putText(img, "Kopek", (100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0))
cv2.imshow('Kopek Text',x)




# threshold
_,thresh_img = cv2.threshold(img1,thresh = 50,maxval = 255,type = cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img,cmap = "gray") #siyah beyaz için
plt.axis("off")
plt.show()

"""
cv2.namedWindow("img",cv2.WINDOW_NORMAL) 
cv2.imshow("img",img)

cv2.namedWindow("img1",cv2.WINDOW_NORMAL) 
cv2.imshow("img1",img1)
"""


# gaussian blur


gb = cv2.GaussianBlur(img1 , ksize = (5,5),sigmaX = 10 ) # yatayda yapılan blur 10 olacak arttıkça daha fazla blurlu olacak
#plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gauss blur")
cv2.namedWindow("gaussian blur",cv2.WINDOW_NORMAL)
cv2.imshow("gaussian blur",gb)



laplacian = cv2.Laplacian(img,ddepth = cv2.CV_64F)
cv2.namedWindow("Laplacian",cv2.WINDOW_NORMAL)
cv2.imshow("Laplacian",laplacian)
# plt.figure(),plt.imshow(laplacian,cmap = "gray"),plt.axis("off"),plt.title("laplacian")


img_hist = cv2.calcHist([img],channels = [0],mask = None,histSize = [256], ranges = [0,256])
plt.figure(),plt.plot(img_hist)


cv2.waitKey(0)

cv2.destroyAllWindows()




#cv2.imwrite("resized_image.jpg", resized_img) #save image

