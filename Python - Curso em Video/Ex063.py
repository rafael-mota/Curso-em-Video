#Sequencia de Fibonacci
num = int(input("Insira quantos valores da sequência de Fibonacci você deseja ver: "))
count = 0
fn = 0
while count < num:
    count += 1
    print(fn, end = " ")
    fn += fn + count