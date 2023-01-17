# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 23:21:37 2023

@author: ozan7
"""
# -hızlı güçlü esnek
# -pandas veri işleme ve analiz kütüphanesi

import pandas as pd

#sözlük oluştur

dictionary  = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
               "yas" : [15,16,17,33,45,66],
               "maas" : [100,150,240,350,110,220]}

veri = pd.DataFrame(dictionary)
print(veri)

#ilk 5 satır
print(veri.head())
print(veri.columns)

# veri bilgisi
print(veri.info())


#istatistiksel özellikler
print(veri.describe())


#yas sütunu
print(veri["yas"])

#sütun eklemek
veri["sehir"] = ["Ankara","İstanbul","İzmir","Eskişehir","Bursa","Antalya"]

#yas sütunu
print(veri.loc[:,"yas"])


#yas sütunu ve 3 satır :3 dersek 3 dahil oluyor numpy'dan farklı
print(veri.loc[:3,"yas"]) 


#yas ve şehir arası sütunu ve 3 satır 
print(veri.loc[:2,"yas":"sehir"]) 

#isim ve yaş
print(veri.loc[:2,["yas","isim"]]) 

#satırları tersten yazdır
print(veri.loc[::-1,:])

#yas sütunu with iloc
print(veri.iloc[:,1])


#ilk 3 satır ve yaş ve isim
print(veri.iloc[:3,[0,1]])



#filtreleme
dictionary  = {"isim" : ["ali","veli","kenan","murat","ayse","hilal"],
               "yas" : [15,16,17,33,45,66],
               "sehir" : ["Ankara","İstanbul","İzmir","Eskişehir","Ankara","Ankara"]}

veri = pd.DataFrame(dictionary)
print(veri)

#yaşa göre filtre yas > 22

filtre1 = veri.yas > 22 
filtrelemis_veri = veri[filtre1]
print(filtrelemis_veri)

# ortalama yaş
ortalama_yas = veri.yas.mean()
print(ortalama_yas)
veri["YAS_GRUBU"] = ["kucuk" if ortalama_yas > i else "buyuk" for i in veri.yas]
print(veri)

# veri birleştirme

sozluk1 = { "isim" : ["ali","veli","kenan"],
           "yas" : [15,16,17],
           "sehir" : ["İzmir","Ankara","Konya"]
           }

veri1 = pd.DataFrame(sozluk1)

sozluk2 = { "isim" : ["murat","ayse","hilal"],
           "yas" : [33,45,66],
           "sehir" : ["Ankara","Ankara","Antalya"]
           }

veri2 = pd.DataFrame(sozluk2)


# dikeyde birleştirme yani veri1 ve veri2 yi alt alta eklemek için
veri_dikey = pd.concat([veri1,veri2],axis = 0)

# yatayda birleştirme yani ilk 3 ismin yanına onun(veri1'in) yaş ve şehrinden sonra diğer 3 (veri2'nin) ismi,yaşını ve şehrini ekledi 
veri_yatay = pd.concat([veri1,veri2],axis = 1)






