# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário = float(input('Qual é o seu salário? R$'))
aumento = salário + (salário * 15 / 100)
print(f'O seu salário com aumento de 15% é de {aumento}')