# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
print('O ângulo de {:.2f} tem SENO de {:.2f}' .format(a, s))
cos = cos(radians(a))
print('O ângulo de {:.2f} tem COSSENO de {:.2f}' .format(a, cos))
tan = tan(radians(a))
print('O ângulo de {:.2f} tem TANGENTE de {:.2f}' .format(a, tan))