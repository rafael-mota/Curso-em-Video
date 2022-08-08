#Validador de Idade de uma pessoa para votação
def voto(idade):
    from datetime import date
    idade_calculada = date.today().year - idade
    if idade_calculada < 16:
        return f"Sua idade é {idade_calculada} anos, então não vota."
    elif 16 <= idade_calculada < 18 or idade_calculada > 65:
        return f"Sua idade é {idade_calculada} anos, o voto é opcional."
    elif idade_calculada >= 18 and idade_calculada <= 65:
        return f"Sua idade é {idade_calculada} anos, o voto é obrigatório."
nascimento = int(input("Digite o ano de seu nascimento: "))
print(voto(nascimento))
