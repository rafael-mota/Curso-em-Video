#Listagem de preços com tuplas
listadeprecos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.00, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print("-"*40)
print(f"{'>>> LISTA DE PREÇOS <<<'.center(40, ' ')}")
print("-"*40)
for i in range(0, (len(listadeprecos)), 2):
    print(f"{listadeprecos[i]:.<30} R${listadeprecos[i+1]:.2f}")
