# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. (se você coloca 3 aspas, é possível adicionar mais linhas no print).

n = int(input('Digite um número inteiro: '))
bases = int(input('''
Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
'''))
print(f'Sua opção: {n}')

if bases == 1:
    print(f'O número {n} em BINÁRIO é {bin(n)[2:]}')
if bases == 2:
    print(f'O número {n} em OCTAL é {oct(n)[2:]}')
if bases == 3:
    print(f'O número {n} em HEXADECIMAL é {hex(n)[2:]}')
else: 
    print('Tente novamente.')