'''
Created on Jan 9, 2024

@author: terlan
B siyahısının 9-dan böyük elementlərinin cəmini və sayını tapmalı.
'''
def nine_plus_cem_ve_sayi(arr):
    elements_gt_nine = [x for x in arr if x > 9]
    sum_gt_nine = sum(x for x in arr if x > 9)
    count_gt_nine = len(elements_gt_nine)
    return sum_gt_nine, count_gt_nine

# Nümunə olaraq bir siyahı yaradırıq
my_list = [4, 17, 2, 9, 15, 6, 3]

# Funksiyamızı çağırırıq və nəticəni çap edirik
result_sum, result_count = nine_plus_cem_ve_sayi(my_list)
print("9-dan böyük elementlərin cəmi:", result_sum)
print("9-dan böyük elementlərin sayı:", result_count)
