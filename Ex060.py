print("CALCULO FATORIAL EM WHILE")
numero = int(input("Insira um número para calcular seu FATORIAL: "))
count = 1
fatorial = 1
print(f"{numero}! =", end=" ")
while count != numero:
    fatorial += fatorial * count
    print(f"{count} {'x' if count < numero else '='}", end=' ')
    count += 1
print(f"{numero} = {fatorial}")

print("\nCALCULO FATORIAL EM FOR")

fatorial2 = 1
print(f"{numero}! =", end=" ")
for i in range(1, numero):
  fatorial2 += i * fatorial2
  print(f"{i}", end=" ")
  print(f"{'x' if i < numero else '='}", end=' ')
print(f"{numero} = {fatorial2}")