# Reescreva a função leiaInt(), incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real digitado foi {n2}')