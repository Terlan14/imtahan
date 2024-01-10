'''
Created on Jan 8, 2024

@author: terlan
Klaviaturadan daxil edilən A matrisinin hər bir sətrindəki ən böyük elementə baş dioqanal elementinin yerini dəyişin
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
# Her bir sətrin ən böyük elementini tapın və baş dioqanal elementlə dəyişin
for i in range(satir_sayisi):
    # Sətrün maksimum elementini tapın
    en_buyuk = max(A[i])
    # Baş köşegenin elementini ən böyük elementlə dəyişin
    A[i][i]=en_buyuk
    

# Dəyişdirilmiş matrisi ekrana yazdırın
print("Dəyişdirilmiş Matris:")
for satir in A:
    print(satir)
