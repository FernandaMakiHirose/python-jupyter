"""
Escopo global: são variáveis que foram definidas e podem ser usadas em todo o programa

Escopo local: são variáveis que não podem ser usadas em todo o programa, porque provavelmente foram definidas dentro de um bloco
"""

numero = 42 # Exemplo de variável global
print(numero) # Vai mostrar o número na tela
print(type(numero)) # Vai mostrar o tipo primitivo do número


if numero > 10:
    novo = numero + 10 # A variável novo está declarada localmente dentro do bloco if. Portanto, é local
    print(novo)