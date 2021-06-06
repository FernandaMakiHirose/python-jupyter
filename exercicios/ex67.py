# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lts=[]
for peso in range(1, 6):
    pessoa = float(input(f'Peso da pessoa {peso}: '))
    lts += [pessoa]
    
print('O maior peso foi: ', max(lts))
print('O menor peso foi: ', min(lts))
