# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

n = str(input('Digite seu nome completo: ')).strip()
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}' .format(n.upper()))
print('Seu nome em minúsculas é {}' .format(n.lower()))
print('Seu nome ao todo tem {} letras' .format(len(n) - n.count(' ')))
print('Seu primeiro nome tem {} letras' .format(n.find(' ')))
