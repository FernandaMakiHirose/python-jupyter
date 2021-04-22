# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

maior = 0
menor = 0
listanum = []

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
            
print('-=' * 30)
print(f'Os valores digitados foram {listanum}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(v)
        print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(v)
