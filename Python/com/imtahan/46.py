'''
Created on Jan 9, 2024

@author: terlan
A siyahısının birinci mənfi elementindən əvvəlki elementlərin hesabi ortasını tapın.
'''
def neg_elem_ortasi(arr):
    neg_index = -1
    neg_sum = 0
    neg_count = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            neg_index = i
            break
    
    if neg_index == -1:
        print("Mənfi element tapılmadı")
        return None
    
    for i in range(neg_index):
        if arr[i] >= 0:
            neg_sum += arr[i]
            neg_count += 1
    
    if neg_count == 0:
        print("Mənfi əvvəlki element yoxdur")
        return None
    
    neg_avg = neg_sum / neg_count
    return neg_avg

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 1, -2, 9, -5, -6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result = neg_elem_ortasi(my_list)
if result is not None:
    print("Mənfi elementdən əvvəlki elementlərin cəmlərinin orta hesabı:", result)
