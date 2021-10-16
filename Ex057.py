#Validador de dados

sexo = str(input("Insira seu sexo [M/F]: ")).strip().upper()[0]

while sexo not in "FfMm":
    if sexo not in "FfMm":
        print("Dados inválidos. Por favor, informe seu sexo: ")
        sexo = str(input("Insira seu sexo [M/F]: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!")

#Guanabara Code
while sexo not in "FfMm":
    sexo = str(input("Dados inválidos. Por favor, insira seu sexo [M/F]: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!")