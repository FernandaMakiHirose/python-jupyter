"""
Dicionários:

Em algumas linguagens de programação, os dicionários python são conhecidos como mapas.
Os dicionários são representados por chaves {}
Não podemos ter chaves repetidas, caso haja chaves com nomes repetidos, os valores vão ser substituídos
A chave e o valor são separados por :, podem ser definidas por qualquer tipo de dados
Os dicionários são representados por chave/valor:

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


Vai pedir para encontrar o país 'ru', se não encontrar vai colocar o valor 'Não encontrado' no lugar
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru', 'Não encontrado') 
print(f'Encontrei o país {pais}')


Verificando se algo está dentro de um elemento:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print('br' in paises) 


Tuplas são interessantes de serem usadas como chaves de dicionários, porque elas são imutáveis:
localidades = {
    ('São Paulo'): 'SP',
    ('Rio de Janeiro'): 'RJ'
}
print(localidades)


Adicionar elementos em um dicionário:
receita = {'janeiro': 100, 'fevereiro': 150}
receita['março'] = 200
print(receita)


Atualizando elementos:
receita = {'janeiro': 100, 'fevereiro': 150}
receita.update({'janeiro': 111})
print(receita)


Remover dados de um dicionário:
receita = {'janeiro': 100, 'fevereiro': 150}
remover = receita.pop('janeiro')
print(receita)

Remover todos os dados de um dicionário:
receita = {'janeiro': 100, 'fevereiro': 150}
receita.clear()
print(receita)


Forma 1 - Copiando um dicionário para outro - Deep Copy:
receita = {'janeiro': 100, 'fevereiro': 150}
novo = receita.copy() 
novo['abril'] = 3 
print(receita)
print(novo)


Forma 2 - Copiando um dicionário para outro - Shallow Copy:
novo = d
print(novo)
novo['d'] = 4
print(d)
print(novo)


Método fromkeys - é necessário ter mais de 1 chave, quando tem apenas 1 chave, todas as letras vão receber o valor:
veja = {}.fromkeys('teste', 'valor')
print(veja)


Veja o método fromkeys com mais de uma chave:
veja = {}.fromkeys(range(0, 11), 'valor range')
print(veja)


Veja o método fromkeys com uma lista dentro:
usuário = {}.fromkeys(['chocolate', 'aveia', 'nescau'], 'comidas')
print(usuário)
"""






