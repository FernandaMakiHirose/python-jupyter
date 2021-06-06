"""
Conhecidos em python como "dicionários"

Iterar em dicionários:

Acessando as chaves:

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita.keys()) 

for chave in receita.keys():
    print(chave)



Acessando os valores:

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita.values())

for valor in receita.values():
    print(valor)



Desempacotamento de dicionários:

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

for chave, valor in receita.items():
    print(f'chave: {chave} e valor: {valor}')
    
print(receita.items())



Soma, valor máximo, valor mínimo, tamanho:

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""

