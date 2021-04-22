# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: mirim.
# Até 14 anos: infantil.
# Até 19 anos: júnior.
# Até 25 anos: sênior.
# Acima de 25 anos: master.
from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} anos')

if idade <= 9:
    print(f'Classificação MIRIM') 
elif idade <= 14:
    print(f'Classificação INFANTIL')
elif idade <= 19:
    print(f'Classificação JÚNIOR')
elif idade <= 25: 
    print(f'Classificação SÊNIOR')
elif idade > 25:
    print(f'Classificação MASTER')