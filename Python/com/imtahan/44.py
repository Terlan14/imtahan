'''
Created on Jan 8, 2024

@author: terlan
'''
# İlk döngüdə ardıcıllıqla ədədləri qəbul edirik
# Tək ədədlərin cəmi, cüt ədədlərin hasilini tapacağıq
tek_cemi = 0
cut_hasili = 1

while True:
    eded = int(input("Doğal ədəd daxil edin (sıfır daxil edərək əməliyyatı dayandırın): "))
    
    if eded == 0:
        break  # Sıfır daxil edildikdə əməliyyatı dayandırır

    if eded % 2 == 0:
        cut_hasili *= eded  # Cüt ədədlərin hasilini tapırıq
    else:
        tek_cemi += eded  # Tək ədədlərin cəmini tapırıq

# Cəmi və hasil hesablanmış dəyərləri ekrana çap edirik
print(f"Tək ədədlərin cəmi: {tek_cemi}")
print(f"Cüt ədədlərin hasilı: {cut_hasili}")
