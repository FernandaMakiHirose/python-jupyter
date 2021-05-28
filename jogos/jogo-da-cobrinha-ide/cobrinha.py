# jogo snake
import pygame
import random

pygame.init()

# cores em rgb usadas no jogo
azul = (50, 100, 213)  
laranja = (205, 102, 0)
verde = (0, 255, 0)
amarelo = (255, 255, 102)

dimensoes = (600, 600) # dimensões do jogo

# VALORES INICIAIS
x = 300 # posição inicial da cobra (centro)
y = 300 # posição inicial da cobra (centro)
d = 20 # tamanho do quadrado
lista_cobra = [[x, y]]
dx = 0 # localização
dy = 0 # localização
x_comida = round(random.randrange(0, 600 - d) / 20) * 20 # valores da comida, pega um valor aleatório para colocar a comida
y_comida = round(random.randrange(0, 600 - d) / 20) * 20 # valores da comida, pega um valor aleatório para colocar a comida
fonte = pygame.font.SysFont("hack", 35)

# vai mostrar as dimensões e 'Snake'
tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake')
tela.fill(azul)
clock = pygame.time.Clock()
def desenha_cobra(lista_cobra):
    tela.fill(azul)
    for unidade in lista_cobra:
        # vai desejar um retângulo
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])

def mover_cobra(dx, dy, lista_cobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # se o evento for clicável
            if event.key == pygame.K_LEFT: # movimentação para à esquerda
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT: # movimentação para à direita
                dx = d
                dy = 0
            elif event.key == pygame.K_UP: # movimentação para cima
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN: # movimentação para baixo
                dx = 0
                dy = d
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy
    lista_cobra.append([x_novo, y_novo])
    del lista_cobra[0]
    return dx, dy, lista_cobra

def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo]) # valores adicionados
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20 # valores da comida
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20 # valores da comida
    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])

    return x_comida, y_comida, lista_cobra

def verifica_parede(lista_cobra):
    head = lista_cobra[-1] # pegando a cabeça da cobra
    # valores 'x' e 'y'
    x = head[0]
    y = head[1]
    
    if x not in range(600) or y not in range(600): # o 'x' e 'y' precisam estar entre 0 a 600
        raise Exception # vai interromper a execução

def verifica_mordeu_cobra(lista_cobra): 
    # se a cabeça do corpo esbarrar em alguma parte do corpo o programa vai ser interrompido
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()
    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
            raise Exception
            
def atualizar_pontos(lista_cobra):
    # funções do pygame que ajudam a escrever coisas na tela
    pts = str(len(lista_cobra) - 1)
    escore = fonte.render("Pontuação: " + pts, True, amarelo)
    tela.blit(escore, [0, 0])

while True: # loop infinito
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(
        dx, dy, x_comida, y_comida, lista_cobra)
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)
    # jogo vai atualizar a cada 5 segundos
    clock.tick(5)
    