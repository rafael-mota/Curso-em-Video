# Criação de tuplas com RANDOM.
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Os valores sorteados foram: {num}.")
print(f"O maior valor é {sorted(num)[0]}.")
print(f"O menor valor é {sorted(num)[-1]}.")