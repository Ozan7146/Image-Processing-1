# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:51:49 2023

@author: ozan
bulanıklaştırma
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("Orijinal"),plt.show()

"""
ortalma bulanıklaştırma yöntemi
ortalama alınır ve merkezi ögenin yerine yerleştirilir

"""
# ksize = kernel size yani bulanıklaştırmayı yapacağım alanın 3*3 lük bir alanın ortalamasını alıp merkezdekini bunla değiştirmesini istiyorum
dst2 = cv2.blur(img , ksize = (3,3))
plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("Ortalama blur")


"""
gaussian blur

"""

gb = cv2.GaussianBlur(img , ksize = (3,3),sigmaX = 7 )
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gauss blur")


"""
medyan blur
"""

mb = cv2.medianBlur(img , ksize = 3 )
plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("Median blur")


def gaussianNoise(image):
    row,col,ch = image.shape
    mean = 0
    var = 0.05 #standart sapmayı önlemek için
    sigma = var**0.5
    
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

#içe aktar ve normalize et
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("Orijinal"),plt.show()
# resim değerleri 0 ile 1 arasında artık eskiden 0 ile 255 arasındaydı

gaussianNoisyImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gauss Noisy"),plt.show()

# noise azaltmak için
# gaus blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage , ksize = (3,3),sigmaX = 7 )
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("with Gauss blur")

# tuz karabiber görüntüsü

def saltPepperNoise(image):
    
    
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    
    # salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p) # beyaz nokta sayısı (ceil)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape] 
    # koordinatları belirlemek için
    noisy[coords] = 1 
    # beyazın karşılığı 1
    # önce sayıyı sonra koordinatlarını rastgele sonra da rengini belirledik
    

    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p)) #  nokta sayısı (ceil) 
    # 1-s_vs_p dememizin sebebi siyah ve beyazın toplamı 1 oluyor 
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape] # koordinatları belirlemek için
    noisy[coords] = 0
    # siyahın karşılığı 0
    return noisy

spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title("SP Image")


# noise u temizlemek için
mb2 = cv2.medianBlur(spImage.astype(np.float32) , ksize = 3 )
plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title("Median blur")














