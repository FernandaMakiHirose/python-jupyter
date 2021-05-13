# O computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
palpite = 0
print('Sou seu computador... Acabei de pensar em um número de 0 a 10. Será que você consegue adivinhar qual foi?')
acertou = False

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if computador > jogador:
        print('Mais')
    elif computador < jogador:
        print('Menos')
    elif computador == jogador:
        print(f'Acertou com {palpite} tentativas. Parabéns!')
