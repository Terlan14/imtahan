'''
Created on Jan 8, 2024

@author: terlan
'''
# A siyahısını yaratmak için kullanıcıdan sətrləri alın
A = [input("Sətri daxil edin: ") for i in range(int(input("Siyahının uzunluğunu daxil edin: ")))]
print("A siyahısı:", A)

# B siyahısını yaratmak için list comprehension kullanın
B = [satir.count('a') for satir in A]
print("B siyahısı:", B)

