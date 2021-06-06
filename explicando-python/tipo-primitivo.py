"""
+ soma
- subtração
* multiplicação
/ divisão
** potência
// é o resultado de uma divisão sem a vírgula
% é o resto, se o resto for igual a 1, o número é ímpar, se for igual a 0 o número é par
== igual


a ordem de precedência (que precisa fazer o cálculo primeiro) é:
1- () parênteses
2- ** potência
3- * multiplicação, / divisão, // resultado da divisão inteira, % resto da divisão inteira (o que aparecer primeiro é o que vai calcular primeiro)
+ adição e - subtração


(com o type conseguimos descobrir qual é o tipo primitivo)
exemplo:
num = 5
type(num)


para números muito grandes, para facilitar nossa leitura podemos separar por underline: (o exemplo abaixo é um milhão)
1_000_000


Para limpar o terminal: Ctrl + L


Float: Tipo real, decimal
As casas decimais são separadas por ponto
Cuidado ao fazer conversão do tipo float para inteiro, porque perde a precisão


É possível fazer dupla atribuição:
valor1, valor2 = 12, 54
- valor1 = 12
- valor 2 = 54


É possível trabalhar com números complexos, basta adicionar o valor 'j':
variável = 5j
type(variável)


Tipo booleano: True (verdadeiro) ou False (falso)
- Sempre apresentam a inicial maiúscula


Vai mostrar que não está ativo:
ativo = False
print(ativo) 


Usando a negação 'not'. Vai mostrar que o usuário está ativo (True):
print(not ativo)


Ou (or): -> Os dois precisam ser falso para ser False, de resto é sempre True
True or True: True
True or False: True
False or True: True
False or False: False


Exemplo (A resposta vai ser True): 
ativo = True
logado = False
print(ativo or logado)


E (and): -> Os dois precisam ser verdadeiro para ser True, de resto é sempre False
True and True: True
True and False: False
False and True: False
False and False: False


String: é tudo que estiver entre aspas simples, aspas duplas, aspas simples triplas, aspas simples triplas, aspas duplas triplas

Se você tem o nome: Fernanda´s Bar, por ter aspas simples, ela fica dentro de aspas duplas

nome = "Fernanda´s Bar"


Para pular uma linha usamos o \n
nome = 'Fernanda \n Maki Hirose'


Para mostrar uma aspa no programa (\" vai mostrar):
nome = 'Fernanda \" Maki Hirose' 


Deixar letras em maiúsculas:
nome = "Fernanda´s Bar"
print(nome.upper())


Deixar letras em minúsculas:
nome = "Fernanda´s Bar"
print(nome.lower())


Transforma em uma lista de strings (vai separar cada letras e espaço)
nome = "Fernanda´s Bar"
print(nome.split())


Slice de string:
nome = "Fernanda´s Bar"
print(nome[0:8]) -> Vai pegar o nome Fernanda, vai do 0 até o 7


print(nome.split()[0]) -> Vai pegar o nome Fernanda´s 


print(nome[::-1]) -> Vai inverter o valor da variável


Substituir algo: 
print(nome.replace('F', 'G')) 
"""
