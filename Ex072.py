# Acesso a tupla como banco de dados.
while True:
  num = " "
  numlst = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")
  while num not in range(21):
    num = int(input("Insira um número entre 0 e 20: "))
  print(f"Você digitou o número {numlst[num]}.")
  continuar = str(input("Deseja continuar? [S/N] >>> ")).strip()[0]
  if continuar in "Nn":
    break
print("PROCESSO ENCERRADO")
