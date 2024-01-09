'''
Created on Jan 9, 2024

@author: terla
'''
def max_ve_indeks(arr):
    max_element = max(arr)
    max_index = arr.index(max_element)
    return max_element, max_index

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 17, 2, 9, 12, 6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result_max, result_index = max_ve_indeks(my_list)
print("Maksimum element:", result_max)
print("Maksimum elementin indeksi:", result_index)
