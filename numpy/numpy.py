# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 22:41:23 2023

@author: ozan7
"""

import numpy as np

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(dizi)

print(dizi.shape) # arrayin boyutu

dizi2 = dizi.reshape(3,5)
print("Şekil: ",dizi.shape)
print("Boyut: ",dizi2.ndim)
print("Veri Tipi: ",dizi2.dtype.name)
print("Boy: ",dizi2.size)

print("Type: ",type(dizi2)) #numpy

dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])
print(dizi2D)


#sıfırlardan oluşan bir array
sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

#birlerden oluşan bir array
bir_dizi = np.ones((3,4))
print(bir_dizi)

#bos array (sıfıra yakın demek boş demek)
bos_dizi = np.empty((3,4))
print(bos_dizi)


#arange (x,y,basamak)

dizi_aralik = np.arange(10,50,5) #50 ye kadar 5 er 5 er arttırarak git
print(dizi_aralik)


# linspace(x,y,basamak) #10 ve 20 arasını 5 e bölüyor
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)

#float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)

#matematiksel işlmemler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)


#dizi elemanı toplama
print(np.sum(a))

#max değer
print(np.max(a))

#min değer
print(np.min(a))

#mean ortalama
print(np.mean(a))

#median ortalama yani ortdaki sayı
print(np.median(a))

#rastgele sayı üretme [0,1] arasında sürekli uniform 3*3
rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

#indeks

dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

#dizinin ilk 4 elemanı
print(dizi[0:4]) 
#0 dahil 4.indeks dahil değil

#dizinin tersi
print(dizi[::-1])

dizi2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(dizi2D)

#dizinin 1.satır ve 1.sütununda bulunana elemanı
print(dizi2D[1,1])

#dizinin 1.sütunu ve tüm satırlarını almak için
print(dizi2D[:,1])

#satır 1 sütun 1,2,3
print(dizi2D[1,1:4])

#dizinin son satır tüm sütunları 
print(dizi2D[-1,:])

#vektör haline getirmek,aynı listeye alıyoruz
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

vektor = dizi2D.ravel()
print(vektor)

#vektördeki maks sayının indeksini bulma

maksimum_sayinin_indeksi = vektor.argmax()
print(maksimum_sayinin_indeksi)
