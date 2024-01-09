'''
Created on Jan 9, 2024

@author: terlan
'''
def neg_elem_evindekiler(arr):
    neg_index = -1

    for i in range(len(arr)):
        if arr[i] < 0:
            neg_index = i
            break
    
    if neg_index == -1:
        print("Mənfi element tapılmadı")
        return 0
    
    sum_before_neg = sum(arr[:neg_index])
    return sum_before_neg

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 7, -2, 9, -5, -6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result = neg_elem_evindekiler(my_list)
print("Birinci mənfi elementdən əvvəlki elementlərin cəmi:", result)
