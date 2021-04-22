# Importando a biblioteca math inteira - peça a raiz quadrada de um número e arredonde ele para cima.

import math
n = float(input('Digite um número para ver a sua raiz quadrada: '))
r = math.sqrt(n)
print(f'A raiz quadrada de {n} é {math.ceil(r)}')