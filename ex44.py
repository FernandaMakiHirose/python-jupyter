# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=' * 10)
print('Analisador de triângulos')
print('-=' * 10)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
if p > s + t and s > p + t and t > s + p:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')