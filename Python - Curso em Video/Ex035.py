print('>>> VERIFIQUE SE É POSSIVEL FORMAR UM TRIÂNGULO <<<')
a = float(input('Digite o comprimento da reta 1: '))
b = float(input('Digite o comprimento da reta 2: '))
c = float(input('Digite o comprimento da reta 3: '))
if ((b - c) < a < (b + c)) == True and ((a - c) < b < (a + c)) == True and ((a - b) < c < (a + b)) == True:
    print('Você consegue formar um triângulo com esses 3 valores!')
else:
    print('Você não consegue formar um triângulo')