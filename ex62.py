# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0 
count = 0
for v in range(1, 7):
    valor = int(input(f'Digite o {v} valor: '))
    if valor % 2 == 0:
        soma = soma + valor
        count = count + 1
print(f'Você informou {count} números pares e a soma foi {soma}')


