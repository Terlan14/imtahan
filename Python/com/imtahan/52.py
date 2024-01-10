'''
Created on Jan 9, 2024

@author: terlan
A siyahısının cüt indeksli elementlərinin cəmini tapmalı.
'''
def cut_indeksli_cem(arr):
    sum_even_index = sum(arr[i] for i in range(len(arr)) if i % 2 == 0)
    return sum_even_index

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 7, -2, 9, -5, -6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result = cut_indeksli_cem(my_list)
print("Cüt indeksli elementlərin cəmi:", result)
