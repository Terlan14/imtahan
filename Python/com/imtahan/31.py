# Örnek A listesi
A = [[3, 8, 2], [5, 12, 7], [9, 4, 6]]

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
