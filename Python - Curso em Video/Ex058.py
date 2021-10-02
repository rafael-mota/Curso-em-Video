#Jogo da adivinhação em While.
import random

print(">>> JOGO DA ADIVINHAÇÃO EM WHILE <<<")

numero_cpu = random.randint(0, 10)
numero = 0
palpites = 0

while numero != numero_cpu:
    numero = int(input("Insira um número: "))
    if numero != numero_cpu:
        if numero < numero_cpu:
          print("Mais... Tente mais uma vez.")
        else:
          print("Menos... Tente mais uma vez.")
    palpites += 1
print(f"Acertou com {palpites} palpites. Parabéns!")