'''
Created on Jan 8, 2024

@author: terlan
Klaviaturadan daxil edilən A matrisinin ən böyük elementini və onun durduğu yeri təyin edin
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

# En büyük elemanı ve konumunu tespit edin
en_buyuk = A[0][0]  # En büyük elemanı A matrisinin ilk elemanı ile başlatın
satir_index = 0
sutun_index = 0

for i in range(satir_sayisi):
    for j in range(sutun_sayisi):
        if A[i][j] > en_buyuk:
            en_buyuk = A[i][j]
            satir_index = i
            sutun_index = j

# Sonucu ekrana yazdırın
print(f"En büyük eleman: {en_buyuk}")
print(f"En büyük elemanın konumu: [{satir_index }][{sutun_index }]")
