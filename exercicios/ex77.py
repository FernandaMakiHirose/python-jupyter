# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) A lista do time.
# b) Os 3 primeiros.
# c) Os 2 últimos colocados.
# d) Os times em ordem alfabética.
# e) A posição do Palmeiras.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio')
print(f'Lista de times: {times}')
print(f'Os três primeiros são: {times[0:3]}')
print(f'Os dois últimos colocados são: {times[2:]}')
print(f'Os times em ordem alfabética é {sorted(times)}')
print(f'O Palmeiras está na posição: {times.index("Palmeiras")+1}º posição')
