'''
Created on Jan 9, 2024

@author: terlan
C siyahısının mənfi elementlərindən D siyahısı düzəltməli.
'''
def duzelt_menfi(arr):
    negative_elements = [x for x in arr if x < 0]
    corrected_list = [x if x >= 0 else 0 for x in arr]
    return negative_elements, corrected_list

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, -7, 2, 9, -5, 6, -3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
negative_elements, corrected_list = duzelt_menfi(my_list)
print("Mənfi elementlər:", negative_elements)
print("Düzəltmiş siyahı:", corrected_list)
