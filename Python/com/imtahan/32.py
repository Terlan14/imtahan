A=[[2,4,-5],[-6,-8,2],[2,3,4]]
yeni_list=[]
for alt_list in A:
    cem=0
    for i in alt_list:
        
        if i>0:
            cem=cem+i
    yeni_list.append(cem)
            
print(yeni_list)
            