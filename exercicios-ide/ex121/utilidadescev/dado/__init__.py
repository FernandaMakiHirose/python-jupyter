# Dentro do pacote utilidadesCeV que criamos no desafio 120, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

def leiaDinheiro(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = input(msg).strip()
            valor = float(n.replace(',', '.'))
        except ValueError:
            print(f"\033[1;33m{n} \033[1;31mé um preço inválido!\033[m")
            continue
        if valor:
            ok = True
        if ok:
            break
    return float(valor)

