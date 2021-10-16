#Sequencia de Fibonacci
print(">>> SEQUÊNCIA DE FIBONACCI <<<")
num = int(input("Insira quantos valores da sequência de Fibonacci você deseja ver: "))
count = 3
t1 = 0
t2 = 1
tr = 0
print(f"{t1} -> {t2} ->", end=" ")
while count <= num:
    tr = t1 + t2
    t1 = t2
    t2 = tr
    print(f"{tr} ->", end=" ")
    count += 1
print('FIM')
