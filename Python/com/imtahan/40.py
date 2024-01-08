'''
Created on Jan 8, 2024

@author: terlan
'''
# Kullanıcıdan N adet kelime alın
N = int(input("Sözlərin sayını daxil edin: "))
sozler = []

for i in range(N):
    soz = input(f"{i+1}. sözü daxil edin: ")
    sozler.append(soz)

# En uzun sözü bulun
en_uzun_soz = max(sozler,key=len)
uzunluk = len(en_uzun_soz)

# Bütün sözləri düzləndirin və * simvolu ilə boşluqları doldurun
duzlenmis_sozler = [soz.ljust(uzunluk, '*') for soz in sozler]

# Düzənlənmiş sözləri ekrana yazdırın
print(f"Ən uzun söz: {en_uzun_soz}")
print("Düzənlənmiş sözlər:")
for soz in duzlenmis_sozler:
    print(soz)
