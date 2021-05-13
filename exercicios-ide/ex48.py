# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 > n2:
    print('O primeiro número é maior')
elif n2 > n1:
    print('O segundo número é maior')