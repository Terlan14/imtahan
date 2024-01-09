'''
Created on Jan 9, 2024

@author: terlan
'''
def musbet_cem(arr):
    cem=0
    for i in arr:
        if i >0:
            cem=cem+i
    return cem
list=[2,3,4,-5,-6,1]
cavab=musbet_cem(list)
print("musbet ededlerin cemi ",cavab)