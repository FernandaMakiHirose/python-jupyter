# faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - quantidade de notas
# - a maior nota
# - a menor nota
# - a média da turma
# - a situação (opcional)

def notas(*notas, sit=True):
    adSituacao = dict()

    total = len(notas)
    adSituacao['Total'] = total

    maior = max(notas)
    adSituacao['Maior'] = maior

    menor = min(notas)
    adSituacao['Menor'] = menor

    soma = sum(notas)
    media = soma / len(notas)
    adSituacao['Média'] = f'{media :.1f}'

    if sit:
        if media >= 7:
            adSituacao['Situação'] = 'Aprovado'
        elif media >= 5:
            adSituacao['Situação'] = 'Razoável'
        else:
            adSituacao['Situação'] = 'Reprovado'

    return adSituacao


# Programa principal...
resposta = notas(5.6, 10, 8.7, 3.3, sit=True)
print(resposta)

