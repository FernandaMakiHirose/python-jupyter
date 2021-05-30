# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('PROCESSANDO...')
sleep(2)
print('-=' * 20)
jogador = float(input('Em que número eu pensei? '))

if jogador == computador:
    print('Parabéns você acertou!')
else:
    print(f'Eu pensei no número {computador} e não no número {jogador}')