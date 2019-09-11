import pygame
import poligonos
import time
import transform

altura = 700
largura = 1280

v0 = [0, 0, 0]
v1 = [100, 0, 0]
v2 = [0, 100, 0]
a0 = [0, 1]
a1 = [0, 2]
a2 = [1, 2]


def desenha(figura, janela):

    arestas = poligonos.get_arestas(figura)

    for i in range(len(arestas)):

        pygame.draw.aaline(janela, (255, 255, 255), (figura.vertices[arestas[i][0]][0],figura.vertices[arestas[i][0]][1]), (figura.vertices[arestas[i][1]][0],figura.vertices[arestas[i][1]][1]))


def main():
    pygame.display.init()
    size = (largura, altura)
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

    #fig = poligonos.Poligono([a0, a1, a2])
    fig1 = poligonos.get_cubo()
    #fig.addVertice([v0, v1, v2])

    background = pygame.Surface(janela.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    fig1 = poligonos.setCentro(fig1)

    fig1 = transform.translate(fig1, largura/2, altura/2, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        janela.blit(background, (0,0))
        #fig1 = transform.scale(fig1, 1.1)
        fig1 = transform.translate(fig1, -largura / 2, -altura / 2, 0)
        fig1 = transform.rotate(fig1, 1, 0, 0, 1/800)
        fig1 = transform.rotate(fig1, 0, 1, 0, 1/800)
        fig1 = transform.rotate(fig1, 0, 0, 1, 1/800)
        fig1 = transform.translate(fig1, largura / 2, altura / 2, 0)
        #desenha(fig, janela)
        #fig = transform.translate(fig, 'x', 0, [a0, a1, a2])
        #fig = transform.translate(fig, 'y', 0, [a0, a1, a2])
        desenha(fig1, janela)

        #poligonos.imprime(fig1)
        poligonos.tamanho_aresta(fig1)
        #fig1 = transform.translate(fig1, 'x', 1, fig1.arestas)
        time.sleep(.001)
        pygame.display.update()


main()