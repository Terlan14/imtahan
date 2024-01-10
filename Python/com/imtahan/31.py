'''
Klaviaturadan daxil edilən A siyahısının hər bir elementi siyahıdır. A siyahısının hər bir elementindəki elementlərinin 
ən böyüyündən yeni siyahı yaratmalı
'''
# Örnek A listesi
A = [[3, 11, 2], [5, 9, 7], [7, 4, 6]]

# Yeni liste yaratmak için boş bir liste oluşturun
yeni_list = []

# Her bir alt liste için işlem yapın
for alt_list in A:
    # Alt listenin en büyük elemanını bulun
    en_buyuk = max(alt_list)
    # Yeni listeye en büyük elemanı ekleyin
    yeni_list.append(en_buyuk)

# Yeni oluşturulan listeyi yazdırın
print(yeni_list)
