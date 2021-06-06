# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} em {atual}')

if idade >= 18:
    print(f'Você precisa se alistar!')
    saldo = idade - 18
    print(f'Você deveria ter se alistado com {saldo} anos')
elif idade < 18:
    print(f'Você ainda não precisa se alistar!')
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos')