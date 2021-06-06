# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {d}Km')
if d <= 200:
    vc = 0.50 * d
    print(f'O preço da sua passagem será de R${vc}')
else: 
    vl = 0.45 * d
    print(f'O preço da sua passagem será de R${vl}')