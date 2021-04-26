"""
1- Tudo que serve para dicionário serve para lista, com execessão das listas serem imutáveis, é necessário adicionar vírgula para números únicos, usa-se parênteses e não copiamos uma tupla usando o copy():

Esses dois exemplos são duas tuplas:
tupla = (1, 2, 3, 4, 5)
tupla = 1, 2, 3, 4, 5

2- Tupla com 1 valor - tuplas são definidas pela vírgula

tupla = (4) -> isso não é uma tupla
tupla = (4,) -> isso é uma tupla por conter a vírgula

3- É possível usar uma tupla com o range

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

4- Desempacotamento da tupla

tupla = ['Fernanda Maki Hirose', '02/06/2003']
nome, datanasc = tupla
print(tupla)

5- Não pode adicionar valor nem tirar valor de uma tupla, já que elas são imutáveis

6- Soma
tupla = [1, 2, 3]
print(sum(tupla))

7- Valor máximo
tupla = [1, 2, 3]
print(max(tupla))

8- Valor mínimo
tupla = [1, 2, 3]
print(min(tupla))

9- Tamanho
tupla = [1, 2, 3]
print(len(tupla))

10- Concatenação de tuplas
tupla1 = [1, 2, 3]
tupla2 = [4, 5, 6]
tupla1 = tupla1 + tupla2
print(tupla1 + tupla2)

11- É possível iterar uma tupla da mesma forma que os dicionários

12- Devemos usar tuplas sempre que não precisarmos modificar os dados, exemplo: meses

13- O acesso aos elementos de uma tupla são semelhantes ao acesso aos dicionários

meses = ('Janeiro', 'Fevereiro')
print(meses[0])

14- Tuplas são mais rápidas que listas

15- Copiando uma tupla - na tupla não temos o problema de Shallow Copy:

tupla = (1, 2, 3)

nova = tupla

outra = (4, 5, 6)
nova = nova + outra

print(nova)
print(tupla)
"""
