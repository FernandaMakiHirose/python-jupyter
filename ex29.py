# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
v = float(input('Digite um valor: '))
raiz = trunc(v)
print(f'O valor digitado foi {v} e sua porção é {(raiz)}')