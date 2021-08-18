cidade = str(input('Digite uma cidade: ')).strip()
sant = 'Santo'
if sant in cidade:
     print(f'Sua cidade tem {sant} no nome!')
else:
     print(f'Sua cidade não tem {sant} no nome!')

#Code Guana
print(cidade[:5].upper() == 'SANTO')