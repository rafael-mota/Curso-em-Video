#Boletim com notas de alunos + cadastro
alunos = []
while True:
    aluno = []
    aluno.append(str(input("NOME: ")))
    aluno.append(list())
    aluno[1].append(float(input("NOTA 1: ")))
    aluno[1].append(float(input("NOTA 2: ")))
    alunos.append(aluno[:])
    aluno.clear()
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Deseja continuar? [S/N] >>> ")).strip()[0]
    if continuar in "Nn":
        break
print("▬"*20)
print(f"No. NOME                     MÉDIA \n{'-'*34}")
for numero, nomes in enumerate(alunos):
    print(f"{numero}   {nomes[0]}                     {(sum(nomes[1])/2):.1f}")
print("▬"*20)

while True:
    menu = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if menu == 999:
        break
    else:
        print(f"Notas de {alunos[menu][0]} são {alunos[menu][1]}")
        print("▬" * 30)