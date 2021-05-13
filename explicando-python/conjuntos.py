"""
Conjuntos: teoria dos conjuntos da matemática
Os conjuntos são chamados de sets
Não possuem valores duplicados, ordenados
Os elementos não são acessados via índices, não são indexados
Eles são bons quando precisa-se armazenar elementos, sem se importar com a ordenação, chaves, valores e itens duplicados
Eles são referenciados por {}
É possível ter qualquer tipo de dado dentro de um set



Um dicionário tem chave e valor, um conjunto tem apenas valor

Isso é um conjunto:

s = {5, 2, 6, 1, 1}
print(type(s))



Podemos verificar se o elemento está no conjunto:

s = {5, 2, 6, 1, 1}
if 0 in s:
    print('Número existente')
else:
    print('Número não existente')



Vamos ver como as listas, tuplas, dicionários e conjuntos se comportam:

Listas aceitam valores duplicados, então temos 10 elementos:

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')


Tuplas aceitam valores duplicados, então temos 10 elementos: 

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')


Dicionários não aceitam chaves duplicadas, então temos 8 elementos:

dicionarios = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionários: {dicionarios} com {len(dicionarios)} elementos')


Conjuntos não aceitam valores duplicados, então temos 8 elementos:

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')


Adicionando dados em um conjunto:
s = {3, 5, 1}
s.add(6)
print(s)


Removendo dados em um conjunto (não retorna o valor):
s = {3, 5, 1}
s.discard(1)


Copiando - Deep Copy:
s = {3, 5, 1}
novo = s.copy()
novo.add(4)
print(novo)
print(s)


Copiando - Shallow Copy:
s = {3, 5, 1}
novo = s
novo.add(4)
print(s)
print(novo)


Remover todos os itens de um conjunto:
s = {3, 5, 1}
s.clear()
print(s)


Mostrando os nomes sem repeti-los (dá para fazer pelo union, mas assim é mais fácil):
python = {'Julia', 'Pedro', 'Fernando'}
java = {'Julia', 'Charlie', 'Fernanda'}
unindo = python | java 
print(unindo)


Mostrando os nomes que se repetem
python = {'Julia', 'Pedro', 'Fernando'}
java = {'Julia', 'Charlie', 'Fernanda'}
unindo = python & java 
print(unindo)


Mostrando os nomes que não se repetem
python = {'Julia', 'Pedro', 'Fernando'}
java = {'Julia', 'Charlie', 'Fernanda'}
unindo = python.difference(java)
unindo2 = java.difference(python)
print(unindo)
print(unindo2)


Soma, valor máximo, valor mínimo, tamanho
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
(print(len(s)))
"""


