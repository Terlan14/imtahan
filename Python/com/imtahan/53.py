'''
Created on Jan 9, 2024

@author: terla
'''
def tek_indeksli_cem(arr):
    sum_odd_index = sum(arr[i] for i in range(len(arr)) if i % 2 != 0)
    return sum_odd_index

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 7, -2, 9, -5, -6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result = tek_indeksli_cem(my_list)
print("Tək indeksli elementlərin cəmi:", result)
