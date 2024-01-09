'''
Created on Jan 9, 2024

@author: terla
'''
def musbet_say(arr):
    count_positive = sum(1 for x in arr if x > 0)
    return count_positive

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, -7, 2, 9, -5, 6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result = musbet_say(my_list)
print("Müsbət elementlərin sayı:", result)
