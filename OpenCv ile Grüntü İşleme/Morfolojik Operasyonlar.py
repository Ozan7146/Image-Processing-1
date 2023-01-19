# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:20:12 2023

@author: ozan

"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("NYC.jpg",0)
plt.figure(),plt.imshow(img, cmap = "gray"),plt.axis("off"),plt.title("Orijinal")

# erozyon
kernel = np.ones((5,5),dtype = np.uint8)
result = cv2.erode(img ,kernel,iterations = 2 )
plt.figure(),plt.imshow(result, cmap = "gray"),plt.axis("off"),plt.title("Erozyon")

# genişleme dilation
result2 = cv2.dilate(img ,kernel,iterations = 1 )
plt.figure(),plt.imshow(result2, cmap = "gray"),plt.axis("off"),plt.title("Genişleme")

# white noise
whiteNoise = np.random.randint(0,2,size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(),plt.imshow(whiteNoise,cmap="gray"),plt.axis("off"),plt.title("White Noise")

noise_img = whiteNoise + img
plt.figure(),plt.imshow(noise_img,cmap="gray"),plt.axis("off"),plt.title("White Noise + picture")

# açılma

opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel) 
plt.figure(),plt.imshow(opening,cmap="gray"),plt.axis("off"),plt.title("acilma")


# black noise
blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = whiteNoise*-255
plt.figure(),plt.imshow(blackNoise,cmap="gray"),plt.axis("off"),plt.title("White Noise")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(),plt.imshow(black_noise_img,cmap="gray"),plt.axis("off"),plt.title("Black Noise")

# kapatma

closing = cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel) 
plt.figure(),plt.imshow(closing,cmap="gray"),plt.axis("off"),plt.title("Kapama")



# morfolojik 
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure(),plt.imshow(gradient,cmap="gray"),plt.axis("off"),plt.title("Gradient")




























