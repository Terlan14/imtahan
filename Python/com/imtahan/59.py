'''
Created on Jan 9, 2024

@author: terlan
C siyahısının minimum elementini  və onun indeksini tapın.
'''
def min_ve_indeks(arr):
    min_element = min(arr)
    min_index = arr.index(min_element)
    return min_element, min_index

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 17, 2, 9, 12, 6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result_min, result_index = min_ve_indeks(my_list)
print("Minimum element:", result_min)
print("Minimum elementin indeksi:", result_index)
