'''
Created on Jan 9, 2024

@author: terlan
B siyahısının müsbət elementlərinin cəmini və sayını tapın.
'''
def musbet_cem(arr):
    cem=0
    say=0
    for i in arr:
        if i >0:
            cem=cem+i
            say=say+1
    return cem,say

list=[2,3,4,-5,-6,1]
cavab_cem,cavab_say=musbet_cem(list)

print("musbet ededlerin cemi ",cavab_cem)
print("musbet ededlerin sayi",cavab_say)
