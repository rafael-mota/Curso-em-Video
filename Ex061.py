#10 termos de uma PA com WHILE
print(">>> 10 PRIMEIROS TERMOS DE UMA PA <<<")
primeiro_termo = int(input("Primeiro termo >>> "))
razao = int(input("Razão >>> "))
count = 1

while count <= 10:
    print(f"{primeiro_termo} →", end = " ")
    primeiro_termo += razao
    count += 1
print("FIM")