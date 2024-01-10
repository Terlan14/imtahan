setir_sayi=int(input("setir sayini daxil edin"))
sutun_sayi=int(input("sutun sayini daxil edin"))
A=[]
for i in range(setir_sayi):
    setir=[]
    for j in range(sutun_sayi):
        element=int(input(f"A[{i}][{j}]"))
        setir.append(element)
    A.append(setir)
print(A)
en_buyuk=A[0][0]
en_kicik=A[0][0]
en_buyuk_indeks=(0,0)
en_kicik_indeks=(0,0)
for i in range(setir_sayi):
    for j in range(sutun_sayi):
        if A[i][j]>en_buyuk:
            en_buyuk=A[i][j]
            en_buyuk_indeks=(i,j)
        if A[i][j]<en_kicik:
            en_kicik=A[i][j]
            en_kicik_indeks=(i,j)

        
print(en_buyuk)
print(en_kicik)