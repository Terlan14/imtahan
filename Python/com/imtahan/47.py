'''
Created on Jan 9, 2024

@author: terlan
A siyahısının birinci mənfi elementindən əvvəlki elementlərin sayını tapın.
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
    
    count = 0
    for i in range(neg_index):
        #if arr[i] >= 0:
            count += 1
    
    return count

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 7,5,6 , -2, 9, -5, -6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result = neg_elem_evindekiler(my_list)
print("Mənfi elementdən əvvəlki elementlərin sayı:", result)
