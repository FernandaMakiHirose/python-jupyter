# Operadores aritméticos - com casas depois da vírgula (só funciona se tiver o format).

v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))

soma = v1 + v2
multiplicação = v1 * v2
potência = v1 ** v2
divisão = v1 / v2
divisãointeira = v1 // v2

print('A soma é {}, o produto é {}, a potência é {}, a divisão é {}, a divisão inteira é {:.2f}' .format(soma, multiplicação, potência, divisão, divisãointeira))