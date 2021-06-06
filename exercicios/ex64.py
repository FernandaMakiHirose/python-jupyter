# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num %  c == 0:
        tot += 1
    else:
        print(f'{c}', end=' ')
print(f'O número {num} foi divisível {tot} vezes')
if tot == 2:
    print('Ele é PRIMO')
else:
    print('Ele NÃO É PRIMO')