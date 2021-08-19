#PRIMEIRO TERMO DE UMA PA
print(f"{'=-='*7} \n10 TERMOS DE UMA PA \n{'=-='*7}")
pterm = int(input("Primeiro termo: "))
raz = int(input("Razão: "))
dec = pterm + (10 - 1) * raz
for i in range(pterm, dec + raz, raz):
    print(f"{i} →", end=" ")
print('FIM')
