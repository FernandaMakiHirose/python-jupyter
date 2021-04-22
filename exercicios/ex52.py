# Equilátero: lados iguais.
# Isósceles: dois lados iguais, um diferente.
# Escaleno: todos os lados diferentes.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 > r2 + r3 and r2 > r1 + r3 and r3 > r1 + r2:
    print('Os segmentos pode formar um triângulo {}', end=' ')
elif r1 == r2 == r3:
    print('ISÓSCELES')
elif r1 != r2 != r3:
    print('ESCALENO')
else:
    print('ISÓSCELES')
    

