'''
Created on Jan 8, 2024

@author: terlan
Siyahı generatorunun köməyi ilə A siyahısı yaradın və siyahı elementlərini klaviaturadan daxil edin. 
Siyahı elementlərinin hər biri sətirdir. Siyahı generatorundan istifadə etməklə A siyahısının hər bir elementindəki “a” 
simvollarının sayından B siyahısı yaratmalı
'''
# A siyahısını yaratmak için kullanıcıdan sətrləri alın
A = [input("Sətri daxil edin: ") for i in range(int(input("Siyahının uzunluğunu daxil edin: ")))]
print("A siyahısı:", A)

# B siyahısını yaratmak için list comprehension kullanın
B = [satir.count('a') for satir in A]
print("B siyahısı:", B)

