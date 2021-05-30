# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input('Quantos R$ você tem na carteira? R$'))
print('Com R${} você consegue comprar US${:.2f}' .format(carteira, carteira/5.596))