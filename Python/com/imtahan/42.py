'''
Created on Jan 8, 2024

@author: terlan
'''
def maksimum_cemi(A, B, C):
    # Her bir siyahının maksimum elementini bulun
    maks_A = max(A)
    maks_B = max(B)
    maks_C = max(C)
    
    # Maksimum elemanların cemini hesaplayın
    cem = maks_A + maks_B + maks_C
    return cem

# Örnek listeler
A = [5, 12, 9, 3]
B = [8, 6, 10, 15]
C = [11, 4, 7, 13]

# Fonksiyonu çağırın ve maksimumların cemini yazdırın
sonuc = maksimum_cemi(A, B, C)
print("Maksimumların cəmi:", sonuc)
