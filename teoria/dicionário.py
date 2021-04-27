"""
Dicionários:

Em algumas linguagens de programação, os dicionários python são conhecidos como mapas.
Os dicionários são representados por chaves {}
Os dicionários são representados por chave/valor:
A chave e o valor são separados por :, podem ser definidas por qualquer tipo de dados

Forma 1:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

Forma 2 - Menos comum:
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

Acessando elementos:

Forma 1 - Acessando via chave, da mesma forma que listas/tuplas
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises['br'])

Forma 2 - Forma recomendada
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises.get('eua'))

"""

