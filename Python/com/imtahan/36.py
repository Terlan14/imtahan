'''
Created on Jan 8, 2024

@author: terlan
'''
# A siyahısını yaratmak için kullanıcıdan tam sayıları alın
A = [int(input("Tam ədədi daxil edin: ")) for _ in range(int(input("Siyahının uzunluğunu daxil edin: ")))]
print("A siyahısı:", A)

# B siyahısını yaratmak için list comprehension kullanın
B = [str(sayi).count('0') for sayi in A]
print("B siyahısı:", B)
