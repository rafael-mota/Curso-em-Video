frase = str(input('Digite uma frase: ')).strip()
print(f'Na frase: {frase} \nConsta {frase.lower().count("a")} letra A')
print(f'Ela aparece pela primeira vez no index {frase.lower().find("a") + 1}')
print(f'E aparece pela ultima vez no index {frase.lower().rfind("a") + 1}')