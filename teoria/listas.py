"""
Podemos adicionar qualquer valor nas listas, as listas aceitam valores repetidos:

lista1 = [1, 2, 3, 4, 5] -> Lista de números

lista2 = ['F', 'e', 'r', 'n', 'a', 'n', 'd', 'a'] -> Lista de strings

lista3 = [] -> Lista vazia

lista4 = list(range(11)) -> Adiciona valores de 0 a 10 na lista


Podemos checar se determinado valor está dentro de uma lista:

lista1 = [1, 2, 3, 4, 5]
if 4 in lista1:
    print('Encontrei o número 4')
else:
    print('Não encontrei o número 4')


Podemos ordenar uma lista - Ordena os números, ordena as strings, porém não de forma correta:

lista1 = [2, 9, 3, 1, 5]
lista1.sort()
print(lista1)


Podemos contar quantas vezes um determinado item aparece em uma lista:

lista2 = ['F', 'e', 'r', 'n', 'a', 'n', 'd', 'a']
print(lista2.count('n'))


Podemos adicionar um elemento na lista com o append, obs: só podemos adicionar um elemento por vez:

lista2 = ['F', 'e', 'r', 'n', 'a', 'n', 'd', 'a']
lista2.append('Olá')
print(lista2)


Para adicionarmos mais de 1 elemento na lista:

lista1 = [2, 9, 3, 1, 5]
lista1.append([99, 100]) -> Adiciona uma lista dentro de uma lista
print(lista1)


Para perguntarmos se mais de um elemento está na lista utilizamos []:

lista1 = [2, 9, 3, 1, 5]
if [99, 100] in lista1:
    print('Encontrei os valores')
else:
    print('Não encontrei os valores')


Para adicionar mais de 1 elemento na lista sem adicionar uma lista dentro de uma lista, o extend não aceita valor único:

lista1 = [2, 9, 3, 1, 5] 
lista1.extend([200, 300])
print(lista1)


Adicionando valor em uma posição da lista, ele não substitui o valor da posição atual, esse valor se desloca para a direita:

lista1 = [2, 9, 3, 1, 5]
lista1.insert(0, 'Novo valor')
print(lista1)


Podemos adicionar duas listas ou mais:

lista1 = [2, 9, 3, 1, 5] 
lista2 = ['F', 'e', 'r', 'n', 'a', 'n', 'd', 'a']
lista3 = lista1 + lista2
print(lista3)


Podemos inverter uma lista:

Forma1:
lista1 = [2, 9, 3, 1, 5] 
lista1.reverse()
print(lista1)

Forma2 - Slice:
lista1 = [2, 9, 3, 1, 5] 
print(lista1[::-1])


Podemos copiar uma lista:

lista1 = [2, 9, 3, 1, 5] 
lista2 = lista1.copy()
print(lista2)


Podemos contar quantos elementos tem dentro da lista:

lista1 = [2, 9, 3, 1, 5] 
print(len(lista1))


Podemos excluir o último elemento de uma lista - ele também retorna o último elemento:

lista1 = [2, 9, 3, 1, 5] 
print(lista1.pop())


Podemos remover um elemento pelo índice - se não existir o índice informado vai dar IndexError:

lista1 = [2, 9, 3, 1, 5] 
print(lista1.pop(0))
print(lista1)


Podemos remover todos os elementos:

lista1 = [2, 9, 3, 1, 5] 
lista1.clear()
print(lista1)


Podemos repetir elementos em uma lista:

lista1 = [2, 9, 3, 1, 5] 
lista1 = lista1 * 3
print(lista1)


Podemos converter uma string para uma lista - o split separa as palavras pelo espaço:

nome = 'Olá, bom dia'
nome = nome.split()
print(nome)


Podemos converter uma string para uma lista - se não tiver espaços podemos dizer qual é o separador dentro do split:

nome = 'Olá,bom dia,tudo,bem?'
nome = nome.split(',')
print(nome)


Convertendo uma lista em uma string - vai atribuir espaço entre as palavras e vai juntar as palavras:

lista1 = ['Programação', 'em', 'Python']
curso = ' '.join(lista1)
print(curso)

Se você quiser separar as palavras por outra forma em vez de espaço, exemplo $:

lista1 = ['Programação', 'em', 'Python']
curso = '$'.join(lista1)
print(curso)


Iterando sobre listas:

Exemplo 1 - calculando a soma de todos os elementos numéricos e mostrando os elementos da lista:

soma = 0
lista1 = [2, 9, 3, 1, 5] 
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

Exemplo 2 - calculando a soma de todos os elementos strings e mostrando os elementos da lista:

soma = ''
lista1 = ['Programando em Python']
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

Exemplo 3:

carrinho = []
usuario = ''

while True:
    usuario = input("Adicione um produto na lista ou digite 'sair' para sair: ")
    if usuario != 'sair':
        carrinho.append(usuario)
    else:
        for usuario in carrinho:
            print(usuario)
        break

Exemplo 4:

cores = ['amarelo', 'branco', 'azul', 'roxo']
print(cores[-1]) -> roxo
print(cores[-2]) -> azul
print(cores[-3]) -> branco
print(cores[-4]) -> amarelo


Achar o índice de um número - ele pega o índice do primeiro valor encontrado:
cores = ['amarelo', 'branco', 'azul', 'roxo']
print(cores.index('amarelo')) -> vai retornar o índice 0


Achar o índice de um número a partir de um índice, caso não tenha o valor na lista vai retornar ValueError:
cores = ['amarelo', 'branco', 'azul', 'roxo', 'amarelo']
print(cores.index('amarelo', 1)) -> vai retornar o índice 4


Achar um índice entre um número e outro:
lista = [1, 2, 3, 4, 5, 3, 6, 3]
print(lista.index(3, 2, 4)) -> vai encontrar índice de 3 entre 2 e 4, vai retornar o valor 2


Revisão do slicing:
lista[início:fim:passo]
range[início:fim:passo]

lista = [1, 2, 3, 4]
print(lista[:4:2]) -> coma do índice 1, até o 3 de 2 em 2
print(lista[1:]) -> vai começar do 2 até o 4
print(lista[::2]) -> vai pegar do 1 até o final de 2 em 2


Realizar a soma de uma lista:
lista = [1, 2, 3, 4]
print(sum(lista))

Pegar o maior valor de uma lista:
lista = [1, 2, 3, 4]
print(max(lista))

Pegar o menor valor de uma lista:
lista = [1, 2, 3, 4]
print(min(lista))

Transformar uma tupla em uma lista:
lista = [1, 2, 3, 4]
tupla = tuple(lista)
print(tupla)

Desempacotamento de listas - as variáveis vão receber os valores das listas:
lista = [1, 2, 3, 4]
num1, num2, num3, num4 = lista
print(num1)
print(num2)
print(num3)

Forma 1 - Deep copy - modificando uma lista ela não afeta a outra

lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)

Forma 2 - Shallow Copy - modificando uma lista ela afeta a outra

lista = [1, 2, 3]
print(lista)
nova = lista
print(nova)
nova.append(4)
print(lista)
print(nova)
"""


