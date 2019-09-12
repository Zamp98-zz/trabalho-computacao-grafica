import pygame
from numba import jit
import poligonos
import transform


altura = 700
largura = 1366

v0 = [0, 0, 0]
v1 = [100, 0, 0]
v2 = [0, 100, 0]
a0 = [0, 1]
a1 = [0, 2]
a2 = [1, 2]


def desenha(figura, janela):
    arestas = poligonos.get_arestas(figura)
    for i in range(len(arestas)):
        pygame.draw.line(janela, (255, 255, 255),
                           (figura.vertices[arestas[i][0]][0], figura.vertices[arestas[i][0]][1]),
                           (figura.vertices[arestas[i][1]][0], figura.vertices[arestas[i][1]][1]),1)


clock = pygame.time.Clock()


def main():
    pygame.display.init()
    size = (largura, altura)
    janela = pygame.display.set_mode(size, 0, 0, 0)
    pygame.display.set_caption("Computação Gráfica")

    # fig = poligonos.Poligono([a0, a1, a2])
    fig1 = poligonos.get_cubo()
    # fig.addVertice([v0, v1, v2])

    background = pygame.Surface(janela.get_size(), flags=pygame.SRCALPHA)
    background = background.convert_alpha()
    background.fill((0, 0, 0))
    fig1 = poligonos.setCentro(fig1)
    cX = fig1.centro[0]
    cY = fig1.centro[1]
    cZ = fig1.centro[2]

    i = 0
    #fig1 = transform.translate(fig1, - cX, - cY, - cZ)
    fig1 = transform.rotate(fig1, 0, 1, 0, 1)
    fig1 = transform.rotate(fig1, 1, 0, 0, 1)
    fig2 = poligonos.get_zig()
    fig2 = poligonos.setCentro(fig2)
    cX1 = fig2.centro[0]
    cY1 = fig2.centro[1]
    cZ1 = fig2.centro[2]
    #fig2 = transform.translate(fig2, 100, 100, 0)
    fig2 = transform.scale(fig2, 20)
    #fig2 = transform.rotate(fig2, 1, 0, 0, 1)
    fig2 = transform.translate(fig2,  -cX1,  -cY1,  -cZ1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #fig1 = transform.translate(fig1, -largura / 2 + cX, -altura / 2 + cY, +cZ)
        #janela.blit(background, (0,0))
        # fig1 = transform.scale(fig1, 1.001)
        #fig1 = transform.translate(fig1, - cX, - cY, - cZ)
        fig2 = transform.translate(fig2, 100, 100, 1)
        fig1 = transform.rotate(fig1, 1, 0, 0, 1 / 200)
        fig1 = transform.rotate(fig1, 0, 1, 0, 1 / 200)
        fig1 = transform.rotate(fig1, 0, 0, 1, 1 / 200)
        #fig2 = transform.rotate(fig2, 1, 0, 0, 1/200)
        #fig2 = transform.rotate(fig2, 0, 1, 0, 1 / 200)
        #fig2 = transform.rotate(fig2, 0, 0, 1, 1 / 200)
        cX = fig1.centro[0]
        cY = fig1.centro[1]
        cZ = fig1.centro[2]
        cX1 = fig2.centro[0]
        cY1 = fig2.centro[1]
        cZ1 = fig2.centro[2]
        print(cX1, cY1, cZ1)
        # print(cX, cY, cZ)
        fig1 = transform.translate(fig1, largura / 2 -cX, altura / 2 -cY, -cZ)
        fig2 = transform.translate(fig2, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
        desenha(fig1, janela)
        desenha(fig2, janela)
        # poligonos.imprime(fig1)
        #poligonos.tamanho_aresta(fig1)
        # time.sleep(.03)



        clock.tick(60)
        poligonos.imprime(fig2)
        print(clock)
        i += 10
        if (i > 700):
            i = 0
        pygame.display.update()
        janela.fill((0, 0, 0, 1))
main()
