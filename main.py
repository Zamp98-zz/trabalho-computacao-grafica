import pygame
import poligonos
import time
import move

v1 = [0, 0, 0]
v2 = [100, 0, 0]
v3 = [0, 100, 0]
a0 = poligonos.Aresta(v1, v2)
a1 = poligonos.Aresta(v1, v3)
a2 = poligonos.Aresta(v2, v3)


def desenha(figura, janela):

    arestas = poligonos.get_arestas(figura)

    for i in range(len(arestas)):
        pygame.draw.aaline(janela, (255, 255, 255), (arestas[i].inicio[0], arestas[i].inicio[1]),
                           (arestas[i].fim[0], arestas[i].fim[1]))


def main():
    pygame.display.init()
    size = (600,400)
    janela = pygame.display.set_mode(size, 0, 0, 0)
    pygame.display.set_caption("Computação Gráfica")

    '''v1 = poligonos.Vertice(50, 50, 50, 1)
    v2 = poligonos.Vertice(100, 200, 60, 1)
    v3 = poligonos.Vertice(100, 300, 30, 1)
    v4 = poligonos.Vertice(100, 400, 30, 1)
    a0 = poligonos.Aresta(v1, v2)
    a1 = poligonos.Aresta(v2, v3)
    a2 = poligonos.Aresta(v1, v3)
    a3 = poligonos.Aresta(v1, v4)
    a4 = poligonos.Aresta(v3, v4)
    a5 = poligonos.Aresta(v2, v4)'''

    fig = poligonos.Poligono([a0, a1, a2])
    fig1 = poligonos.get_cubo()
    fig.addVertice([v1, v2, v3])

    background = pygame.Surface(janela.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    fig = move.translate(fig, 'x', 100, [a0, a1, a2])
    fig = move.translate(fig, 'y', 100, [a0, a1, a2])

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        janela.blit(background, (0,0))
        desenha(fig, janela)
        fig = move.translate(fig, 'x', 0, [a0, a1, a2])
        fig = move.translate(fig, 'y', 0, [a0, a1, a2])
        desenha(fig1, janela)
        fig1 = move.translate(fig1, 'y', 1, fig1.arestas)
        time.sleep(1)
        pygame.display.update()


main()