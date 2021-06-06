# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

pt = int(input('Diga qual é o primeiro termo: '))
razão = int(input('Diga a razão: '))
décimo = pt + (10 - 1) * razão
for a in range(pt, razão + décimo, razão):
    print(a, end=' ')
print('ACABOU')