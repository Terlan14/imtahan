'''
Created on Jan 9, 2024

@author: terla
'''
def five_to_fifteen_cemi(arr):
    elements_between_5_and_15 = [x for x in arr if 5 < x < 15]
    sum_between_5_and_15 = sum(elements_between_5_and_15)
    return sum_between_5_and_15

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 17, 2, 9, 12, 6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result_sum = five_to_fifteen_cemi(my_list)
print("5-dən böyük və 15-dən kiçik elementlərin cəmi:", result_sum)
