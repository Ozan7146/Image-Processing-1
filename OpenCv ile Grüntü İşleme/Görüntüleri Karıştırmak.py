# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 01:41:51 2023

@author: ozan
Görüntü Karıştırma
"""
# opencv BGR olarak yüklediği için renkleri değiştirmemiz lazım
import cv2
import mapplotlib as plt

img1 = cv2.imread("img2.jpg")
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2= cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

"""
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)
"""

# Aynı boyutta olması lazım
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1,(600,600))
img2 = cv2.resize(img1,(600,600))

print(img1.shape)
print(img2.shape)

plt.figure()
plt.imshow(img1)


plt.figure()
plt.imshow(img2)

#  Karıştırılmış resim = alpha*img1 + beta*img2
blended = cv2.addWeighted(src1 = img1,alpha = 0.5,src2 = img2, beta=0.5,gamma =0)
plt.figure()
plt.imshow(blended)












