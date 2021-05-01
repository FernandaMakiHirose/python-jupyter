# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual é o valor da casa? R$'))
salário = float(input('Qual é o salário do comprador? R$'))
ano = int(input('Quantos anos de financiamento? '))
prestação = casa / (ano * 12) 
mínimo = (salário * 30) / 100
print('Para pagar uma casa de {:.2f} em {:.2f} anos a prestação será de {:.2f}' .format(casa, ano, prestação))
if prestação <= mínimo:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')