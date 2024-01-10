'''
Created on Jan 8, 2024

@author: terlan
Klaviaturadan daxil edilən siyahıda ardıcıl iki sıfırın olduğunu yoxlayın
'''
# Kullanıcıdan sıyahıyı qəbul edin
siyahı = input("Natural ədədlərin siyahısını daxil edin (nöqtələ ayrılmalıdır): ")

# Əgər ardıcıllıqla iki sıfır varsa, bu durumu yoxlayın
if '00' in siyahı:
    print("Ardıcıllıqla iki sıfır var.")
else:
    print("Ardıcıllıqla iki sıfır yoxdur.")
