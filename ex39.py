# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('Multado!')
    m = (v - 80) * 7
    print(f'Você deve pagar uma multa de R${m}')
print('Tenha um bom dia.')