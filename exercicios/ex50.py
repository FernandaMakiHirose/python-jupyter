# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: reprovado.
# Média entre 5.0 e 6.9: recuperação.
# Média entre 7.0 ou superior: aprovado.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

média = (n1 + n2) / 2
if média < 5:
    print('Reprovado')
elif média >= 5 and média <= 6.9:
    print('O aluno está de recuperação!')
elif média >= 7:
    print('O aluno está aprovado') 
    
print('Tirando {:.2f} e {:.2f} sua média é de {:.2f}' .format(n1, n2, média))