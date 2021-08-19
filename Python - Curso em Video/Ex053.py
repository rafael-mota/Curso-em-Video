#VERIFICADOR DE PALÍNDROMO
#apos a sopa
#a sacada da casa
#a torre da derrota
#o lobo ama o bolo
#anotaram a data da maratona

print(">>> VERIFICADOR DE PALÍNDROMO <<<")
nome = str(input("Digite uma frase: ")).upper().strip()
nomelst = nome.split()
nomejoin = ''.join(nomelst)
revers = nomejoin[::-1]
if nomejoin == revers:
    print('A frase inserida é um PALÍNDROMO!')
else:
    print("A frase não é um palíndromo")

#Guanabara Code
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase inserida é um PALÍNDROMO!')
else:
    print("A frase não é um palíndromo")