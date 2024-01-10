'''
Created on Jan 8, 2024

@author: terlan
Klaviaturadan daxil edilən A matrisinin ən böyük elementi ilə ən kiçik elementinin yerini dəyişin
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
        element = float(input(f"Element [{i}][{j }]: "))
        satir.append(element)
    A.append(satir)

# En büyük ve en küçük elemanları bulun
en_buyuk = A[0][0]
en_kucuk = A[0][0]
buyuk_indeks = (0, 0)
kucuk_indeks = (0, 0)

for i in range(satir_sayisi):
    for j in range(sutun_sayisi):
        if A[i][j] > en_buyuk:
            en_buyuk = A[i][j]
            buyuk_indeks = (i, j)
        if A[i][j] < en_kucuk:
            en_kucuk = A[i][j]
            kucuk_indeks = (i, j)

# En büyük ve en küçük elemanların yerlerini değiştirin
A[buyuk_indeks[0]][buyuk_indeks[1]] = en_kucuk
A[kucuk_indeks[0]][kucuk_indeks[1]] = en_buyuk

# Değiştirilmiş matrisi ekrana yazdırın
print("Değiştirilmiş Matris:")
for satir in A:
    print(satir)
