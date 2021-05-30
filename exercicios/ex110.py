# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def analise(nome, gols):
    if not nome:
        nome = '<desconhecido>'
    if not gols or not gols.isnumeric():
        gols = 0
    print('-' * 50)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

j = str(input('Nome do jogador: ')).strip()
g = str(input('Número de gols: ')).strip()
analise(j, g)
