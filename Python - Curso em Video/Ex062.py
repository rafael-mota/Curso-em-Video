#10 termos de uma PA com WHILE
print(">>> TERMOS DE UMA PA AVANÇADO <<<")
primeiro_termo = int(input("Primeiro termo >>> "))
razao = int(input("Razão >>> "))
count = 0
termos = 10

while count <= termos:
    if count == termos:
        print("PAUSA")
        novo_termos = int(input("\nQuantos termos você quer mostrar a mais? >>> "))
        if novo_termos > 0:
            termos += novo_termos
        else:
            break
    print(f"{primeiro_termo} →", end=" ")
    primeiro_termo += razao
    count += 1
print(f"Progressão finalizada com {count} termos mostrados")