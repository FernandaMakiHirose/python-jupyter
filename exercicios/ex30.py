# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot 
co = float(input('O cateto oposto é: '))
ca = float(input('O cateto adjacente é: '))
hi = hypot(co, ca)
print('A hipotenusa é {:.2f}' .format(hi))