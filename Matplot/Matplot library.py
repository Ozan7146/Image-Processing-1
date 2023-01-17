# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:28:24 2023

@author: ozan
matplot lib
"""

#veri görselleştirme = bilgi ve verilerin grafiksel temsilidir.
#görüntüleri anlamlandırmakla başlayacağız


import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])

plt.figure() # tablolar karışmasın diye bu tabloyu açma
plt.plot(x,y, color ="red" , alpha = 0.7 , label = "line")
 # alpha = 0 tamamen saydam, alpha = 1 en neti

#nokta ekledik 
plt.scatter(x,y,color = "blue" ,alpha = 0.4 , label = "scatter")

# başlıklar eklemek için
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")

#çizgi eklemek için tüm grafiğe (kareli kağıt gibi)
plt.grid(True)

# x ekseninin değer aralığını arttırmak için
plt.xticks([0,1,2,3,4,5])

#labelin görülebilmesi için
plt.legend()
plt.show() # bu da tabloyu kapama



fig, axes = plt.subplots(2,1, figsize = (9,7)) # 2 satır 1 sütun
fig.subplots_adjust(hspace = 0.5) # iki resim arasında boşluk olsun

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")


axes[1].scatter(y,x)
axes[1].set_title("sub-2")
axes[1].set_ylabel("sub-2 y")
axes[1].set_xlabel("sub-2 x")



#random resim
plt.figure()
img = np.random.random((50,50))
plt.imshow(img, cmap = "gray") # 0 (siyah)  1(beyaz) -> 0.5 (gri) buraya gray yazmazsak kendisi default olarak renkli bir değer kullanır
#plt.axis("off")
plt.show()




























