'''
Created on Jan 9, 2024

@author: terla
'''
def duzelt_musbet(arr):
    positive_elements = [x for x in arr if x > 0]
    corrected_list = [x if x <= 0 else 0 for x in arr]
    return positive_elements, corrected_list

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, -7, 2, 9, -5, 6, -3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
positive_elements, corrected_list = duzelt_musbet(my_list)
print("Müsbət elementlər:", positive_elements)
print("Düzəltmiş siyahı:", corrected_list)
