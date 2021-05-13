# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Qual é o preço do seu produto? R$'))
novo = p - (p * 5 / 100)
print('Com o desconto de 5% o preço do seu produto fica {:.2f}' .format(novo)) 