"""
Ranges são utilizados para gerar sequências numéricas de maneira específica
1- Se não especificar onde ele vai começar, ele sempre vai começar em 0
2- Se você especificar o número, ele vai começar do número até o número final
3- Temos o passo especificado pelo usuário
4- Temos a forma inversa, tem o valor final primeiro, depois o valor inicial e o passo negativo

Exemplo 1:
for num in range(11):
    print(num)

 Vai mostrar do número 0 até o 10


 Exemplo 2:
 for num in range(1, 11):
     print(num)
     
Vai mostrar do número 1 até o 10


Exemplo 3:
for num in range(1, 11, 2):
    print(num)

Vai mostrar do 1 até o 10 de 2 em 2 

Exemplo 4:
for num in range(10, 0, -1):
    print(num)

Vai mostrar de 10 até 1 de 1 em 1
"""
