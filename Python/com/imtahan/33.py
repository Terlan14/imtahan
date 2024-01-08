'''
Created on Jan 8, 2024

@author: terlan
Klaviaturadan daxil edilən A siyahısının hər bir elementi sətirdir. Sətirlər bir sözdən ibarətdir.
Simvollarının sayı tək olan sövəri və həmin sözün ortasındakı simvolu ekrana verməli
'''
# Klavyeden A listesini alın
A = []
n = int(input("Sətrlərin sayını daxil edin: "))

for i in range(n):
    satir = input("Sətri daxil edin: ")
    A.append(satir)

# Her bir sətri yoxlayın
for satir in A:
    # Sətrin uzunluğunu tapın
    uzunluk = len(satir)
    
    # Sətrin uzunluğu tək olduğunda işləm edin
    if uzunluk % 2 != 0:
        # Sətrin ortasındakı simvolun indeksini tapın
        orta_indeks = uzunluk // 2
        orta_simvol = satir[orta_indeks]
        
        # Ortadakı simvolu və sətri ekrana çap edin
        print(f"Ortadakı simvol: {orta_simvol}, Sətir: {satir}")
