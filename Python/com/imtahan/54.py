'''
Created on Jan 9, 2024

@author: terlan
A siyahısının mənfi elementlərinin cəmini və sayını tapın.
'''
def menfi_cem_ve_say(arr):
    negative_sum = sum(x for x in arr if x < 0)
    negative_count = sum(1 for x in arr if x < 0)
    return negative_sum, negative_count

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, -7, 2, 9, -5, 6, -3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result_sum, result_count = menfi_cem_ve_say(my_list)
print("Mənfi elementlərin cəmi:", result_sum)
print("Mənfi elementlərin sayı:", result_count)
