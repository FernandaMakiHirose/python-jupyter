"""
-- Exemplo 1 - Iterando uma string: --
nome = 'Fernanda'

for letra in nome:
    print(letra, end='')

(Vai mostrar as letras do nome 'Fernanda', para não deixar uma embaixo da outra utilizou-se o end='')




-- Exemplo 2 - Iterando uma lista: --
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for numero in lista:
    print(numero)

(Vai mostrar os números da lista um embaixo do outro)




-- Exemplo 3 - Iterando um range: --
for numero in range(1, 10):
    print(numero)

(Vai mostrar do número 1 até o 9)
range(valor inicial, valor final - 1)




-- Exemplo 4 - Enumerate para pegar o índice ou o valor --

nome = 'Fernanda'
for i, v in enumerate(nome):
    print(v)

(i = índice
v = valor
vai ver o índice ou o valor de nome
no print pediu para ver o valor, podemos substituir também pelo 'i' para ver o índice)




-- Exemplo 5 - Enumerate para pegar o índice e o valor ao mesmo tempo --

nome = 'Fernanda'
for valor in enumerate(nome):
    print(valor)




-- Exemplo 6 - Perguntando quantas vezes quer rodar + calculando a soma dos números informados --

quantidade = int(input('Quantas vezes o loop deve rodar? '))
soma = 0

for n in range(1, quantidade + 1):
    num = int(input(f'Informe o {n}/{quantidade} valor: '))
    soma += 1
print(f'A soma é {soma}')




-- Exemplo 7 - Unicode --
https://emojipedia.org/ 
Original: U+1F605
Modificado: U0001F605 (adicione U000 + o código unicode sem o U+)

for _ in range(3):
    for num in range(1, 10):
        print('\U0001F605' * num)
        
(1- O primeiro for vai repetir 3 vezes
2- O segundo for vai de 1 até 9, os quais vão se repetir 3 vezes
3- Vai mostrar o emoji modificado vezes o número de vezes do num)



-- DICAS/Pycharm --
1- Ctrl + clique no print = você vai ver a documentação do print
2- Quando não queremos adicionar um valor, podemos ignorar ele com underline
"""
