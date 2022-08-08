# Analisando e gerando dicionários
def turma(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param: notas: uma ou mais notas dos alunos (aceita várias entradas);
    :param: sit: valor opcional, indicando se deve ou não mostrar a situação da turma com base na média de notas;
    :return: dicionário com informações sobre a situação da turma.
    """

    banco_de_notas = dict()
    notas_organizadas = sorted(notas)
    media_de_notas = sum(notas_organizadas) / len(notas_organizadas)

    banco_de_notas["total"] = len(notas_organizadas)
    banco_de_notas["maior"] = notas_organizadas[-1]
    banco_de_notas["menor"] = notas_organizadas[0]
    banco_de_notas["média"] = media_de_notas

    if sit:
        if media_de_notas < 5:
            banco_de_notas["Situação"] = "RUIM"
        elif 5 <= media_de_notas <= 7:
            banco_de_notas["Situação"] = "RAZOÁVEL"
        elif media_de_notas > 7:
            banco_de_notas["Situação"] = "BOA"

    return banco_de_notas


resp = turma(5.5, 7, 10, 2, 10, 3, 10, sit=True)
print(resp)
