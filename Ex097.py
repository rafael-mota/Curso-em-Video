#Escrita adaptavel com funções
def escreva(palavra):
    print("~" * (len(palavra)+4))
    print(f"  {palavra}  ")
    print("~" * (len(palavra)+4))


escreva(str(input("Escreva uma palavra: ")))