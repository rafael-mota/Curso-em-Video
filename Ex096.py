#Função com calculo de area
print("Controle de Terrenos")
def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno {largura} x {comprimento} é de {area}m²")


area(float(input("LARGURA [M]: ")), float(input("COMPRIMENTO [M]:")))