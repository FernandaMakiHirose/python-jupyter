# Tabuada com laços.

num = float(input('Digite um número: '))
for tabuada in range(1, 11):
    print('{:.2f} x {:.2f} = {:.2f}' .format(num, tabuada, num * tabuada))