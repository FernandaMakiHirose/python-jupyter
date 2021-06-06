"""
https://docs.python.org/3/library/collections.html 

Módulos Collections - Counter

O Counter conta quantas vezes aparece certo valor:

Exemplo 1 - Contando números - Vai contar quantas vezes os números apareceram:

from collections import Counter
lista = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
res = Counter(lista)
print(type(res))
print(res)

Exemplo 2 - Contando strings - Vai contar quantas vezes as letras da palavra aparecem:

from collections import Counter
tupla = ('Fernanda')
nome = Counter(tupla)
print(type(nome))
print(nome)


Exemplo 3 - Vai contar quantas vezes as palavras da lista apareceram: 

from collections import Counter
texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

lista = texto.split()
contador = Counter(lista)
print(contador)


Exemplo 4 - Encontrando as 5 palavras com mais ocorrências:

from collections import Counter

texto = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

contador = Counter(texto)
print(contador.most_common(5))
"""
