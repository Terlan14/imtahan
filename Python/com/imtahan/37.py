'''
Created on Jan 8, 2024

@author: terlan
Klaviaturadan daxil edilən A matrisinin baş dioqanal elementindən aşağıda yerləşən elementlərinin cəmini tapın
'''
# Matrisin satır ve sütun sayısını alın
satir_sayisi = int(input("Matrisin satır sayısını daxil edin: "))
sutun_sayisi = int(input("Matrisin sütun sayısını daxil edin: "))

# Matrisi kullanıcıdan alın
A = []
print("Matrisi doldurun:")
for i in range(satir_sayisi):
    satir = []
    for j in range(sutun_sayisi):
        element = float(input(f"Element [{i }][{j }]: "))
        satir.append(element)
    A.append(satir)

# Baş köşegenin altındaki elemanların toplamını hesaplayın
toplam = 0
for i in range(satir_sayisi):
    for j in range(sutun_sayisi):
        if i > j:  # Baş köşegenin altındaki elemanları kontrol eder
            toplam += A[i][j]

# Sonucu ekrana yazdırın
print("Baş köşegenin altındaki elementlerin toplamı:", toplam)
