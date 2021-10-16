# Analise de produtos e preço
total_gasto = 0
produtos_caros = 0
preco_barato = 0
produto_barato = " "
print(">>> ANÁLISE DE PRODUTOS <<<")
while True:
    nome_produto = str(input("Insira o nome do produto: ")).strip().capitalize()
    preco = float(input("Insira o preço do produto: R$"))
    total_gasto += preco
    # Análise do produto acima de 1000 reais
    if preco >= 1000:
        produtos_caros += 1
    if produto_barato != nome_produto:
      if preco_barato == 0 or preco < preco_barato:   
        produto_barato = nome_produto  
        preco_barato = preco
    continuar = " "
    while continuar not in "SsNn":
      continuar = str(input("Quer continuar? {S/N} >>> ")).strip()[0]
    if continuar in "Nn":
        break
print("PROCESSO DE ANÁLISE FINALIZADO")
print(f"O total gasto foi de {total_gasto:.2f}.")
print(f"{produtos_caros} produto(s) custaram 1000 reais ou mais.")
print(f"O produto mais barato é {produto_barato} e custou R${preco_barato:.2f}")
