# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 22:06:20 2023

@author: ozan
bilgsayarımızdaki klasörlerde dolaşmamızı sağlayan resimleri içeri yüklerken veya kaydederken kullanacağımız kütüphane
"""

import os

print(os.name)

currentDir = os.getcwd()
print(currentDir)

#new folder
folder_name = "yeni1"
os.mkdir(folder_name)

new_folder_name = "yeni2"
os.rename(folder_name, new_folder_name)

# !!!Burdaki yazan işlemlerin gerçekleşmesi için aynı yerde (adreste) olmaları lazım sağdaki(outputtaki print(currentDir) bunun sayesinde çıkan ) ve yukardaki(C: ....) adresi

#farklı bir klasöre girmek için
os.chdir(currentDir+"\\"+ new_folder_name)
print(os.getcwd())
#chdir = change directory


os.chdir(currentDir)
print(os.getcwd())

#içindeki dosyaları gösteriyor
files = os.listdir()
print(files)

for f in files:
    if f.endswith(".py"):
        print(f)
        
# remove directory        
os.rmdir(new_folder_name)

#şuan kullandığımız yani açık olan klasörde dolaş ve print et diyoruz
for i in os.walk(currentDir):
    print(i)


#aradığımız dosya var mı yok mu ona bakıyoruz
os.path.exists("os.py") #True
os.path.exists("o2s.py") #False


