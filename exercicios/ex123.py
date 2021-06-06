# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False): # o show é o parâmetro opcional e ele começa com false porque não quer mostrar o fatorial
    """
    -> Calcule o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1 # criou uma variável f, que começa com 1
    for c in range(n, 0, -1): # vai começar do número até o 0, decrescente
        if show: # se o show
            print(c, end='') # vai mostrar o número
            if c > 1: # se for maior que 1
                print(' x ', end='') # vai mostrar o vezes
            else: # se não
                print(' = ', end='') # se for igual a 1, significa que é o último número
        f *= c # vai adicionar o fatorial no c
    return f # vai mostrar o valor de f

print(fatorial(5, show=True)) #vai mostrar o fatorial do 5, o show=True vai mostrar o valor mostrando na tela
help(fatorial)