# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

jogador = int(input('Qual é a sua jogada? '))
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-=' * 10)
print('O computador jogou {}' .format(itens[computador]))
print('O jogador jogou {}' .format(itens[jogador]))
print('-=' * 10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ GANHOU')
    else: 
        print('Jogada inválida')
elif computador == 2:
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')
    else:
        print('Jogada inválida')

