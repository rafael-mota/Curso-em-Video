from math import hypot
#Comprimento da hipotenusa - Triangulo retângulo
catopo = float(input('Insira a area do cateto oposto: '))
catadj = float(input('insira a area do cateto adjacente: '))
print(hypot(catopo, catadj))