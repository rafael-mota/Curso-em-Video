#Analise de expressões
expressao = input("Digite uma expressão para valida-lá: ").strip().lower()
lista = []
for i in expressao:
    lista.append(i)
if lista.count("(") / lista.count(")") == 1:
    print("Sua expressão está CORRETA!")
else: #lista.count("(") % lista.count(")") == 1:
    print("Sua expressão está ERRADA!")
