'''
Created on Jan 8, 2024

@author: terlan
Klaviaturadan daxil edilən N ədəd sətrin hər birindəki boşluqların sayını tapmalı
'''
N = int(input("Sətrlərin sayını daxil edin: "))
satir_sayisi = []

# Kullanıcıdan sətrləri alın ve boşluq sayısını hesaplayın
for i in range(N):
    satir = input(f"{i+1}. sətri daxil edin: ")
    bosluq_sayisi = satir.count(' ')  # Boşluk sayısını bulun
    satir_sayisi.append(bosluq_sayisi)

# Her bir sətrdəki boşluq sayısını ekrana yazdırın
for i, bosluqlar in enumerate(satir_sayisi):
    print(f"{i+1}. sətrdəki boşluq sayısı: {bosluqlar}")
