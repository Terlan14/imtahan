'''
Created on Jan 8, 2024

@author: terlan
'''

A=[]
yeni_siyahi=[]
n=int(input("setrlerin sayini daxil edin"))
for i in range (n):
    setr=input("setri daxil edin")
    A.append(setr)
    say=0
    for j in setr :
        say=say+1
    yeni_siyahi.append(say)
print(yeni_siyahi)  