# Calcule a média de um aluno e diga se ele passou ou não.

n = float(input('Digite a sua nota: '))
n2 = float(input('Digite a sua segunda nota: '))
média = (n + n2) / 2
print('A sua média é {:.2f}' .format(média))
if média >= 6:
    print('Você passou!')
else: 
    print('Você não passou!')