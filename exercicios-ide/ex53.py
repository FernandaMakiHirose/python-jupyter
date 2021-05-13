# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto.
# À vista no cartão: 5% de desconto.
# Em até 2x no cartão: preço formal.
# 3x ou mais no cartão: 20% de juros.

print('=' * 5, 'LOJA GUANABARA', end=' ')
print('=' * 5)

preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

opção = int(input('Qual é a sua opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('O total a se pagar é de {:.2f} reais' .format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {:.2f}x de R${:.2f} com juros.' .format(totalparc, parcela)) 
    print('O preço a se pagar é de {:.2f} reais' .format(parcela)) 
else: 
   total = 0
   print('Opção inválida de pagamento. Tente novamente.')
print('Sua compra de {:.2f} reais vai custar {:.2f} no final' .format(preço, total)) 
