# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:12:35 2023

@author: ozan
Histogram
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("RED.jpg")
img_vis = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img_vis)

print(img.shape)
# 0 gray scale olduğunu göseriyor
img_hist = cv2.calcHist([img],channels = [0],mask = None,histSize = [256], ranges = [0,256])
print(img_hist.shape)
plt.figure(),plt.plot(img_hist)

# rengini grafiğe dökme
color = ("b","g","r")
plt.figure()
for i, c in enumerate(color):
    hist = cv2.calcHist([img],channels = [i],mask = None,histSize = [256], ranges = [0,256])
    plt.plot(hist,color = c)

# rengini normale çevirme
golden_gate = cv2.imread("Golden Gate.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate,cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(golden_gate_vis)

print(golden_gate.shape)

# Maskeleme bir parçasını alma
mask = np.zeros(golden_gate.shape[:2],np.uint8)
plt.figure(),plt.imshow(mask,cmap= "gray")

mask[120:180,20:100 ] = 255
plt.figure(),plt.imshow(mask,cmap= "gray")



masked_img_vis = cv2.bitwise_and(golden_gate_vis,golden_gate_vis,mask = mask)
plt.figure(),plt.imshow(masked_img_vis,cmap= "gray")


masked_img = cv2.bitwise_and(golden_gate,golden_gate,mask = mask)
masked_img_hist = cv2.calcHist([golden_gate],channels = [0],mask = mask,histSize = [256], ranges = [0,256])
plt.figure(),plt.plot(masked_img_hist)


# histogram eşitleme
# karşıtlık arttırma kontrast sayesinde

img1 = cv2.imread("bird.jpg",0)
plt.figure(), plt.imshow(img1,cmap= "gray")
# siyah beyaz olduğu için bir tane channel var zaten 
img_hist =  cv2.calcHist([img1],channels = [0],mask = None,histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img1)
plt.figure(),plt.imshow(eq_hist,cmap = "gray")

eq_img_hist =  cv2.calcHist([eq_hist],channels = [0],mask = None,histSize = [256], ranges = [0,256])
plt.figure(), plt.plot(eq_img_hist)
