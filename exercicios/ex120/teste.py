# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 116, 117 e 119 para o primeiro pacote e mantenha tudo funcionando.

from ex120.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 20, 12)
