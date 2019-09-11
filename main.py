import pygame
import poligonos
import time
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

        pygame.draw.aaline(janela, (255, 255, 255), (figura.vertices[arestas[i][0]][0],figura.vertices[arestas[i][0]][1]), (figura.vertices[arestas[i][1]][0],figura.vertices[arestas[i][1]][1]))


def main():
    pygame.display.init()
    size = (largura, altura)
    janela = pygame.display.set_mode(size, 0, 0, 0)
    pygame.display.set_caption("Computação Gráfica")

    #fig = poligonos.Poligono([a0, a1, a2])
    fig1 = poligonos.get_cubo()
    #fig.addVertice([v0, v1, v2])

    background = pygame.Surface(janela.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    fig1 = poligonos.setCentro(fig1)
    centro = len(fig1.vertices)
    centro = centro - 1
    cX = fig1.vertices[centro][0]
    cY = fig1.vertices[centro][1]
    cZ = fig1.vertices[centro][2]

    i = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        janela.blit(background, (0,0))
        #fig1 = transform.scale(fig1, 1.001)

        fig1 = transform.rotate(fig1, 1, 0, 0, 1/200)
        fig1 = transform.rotate(fig1, 0, 1, 0, 1/200)
        fig1 = transform.rotate(fig1, 0, 0, 1, 1/200)

        cX = fig1.vertices[centro][0]
        cY = fig1.vertices[centro][1]
        cZ = fig1.vertices[centro][2]
        #print(cX, cY, cZ)
        fig1 = transform.translate(fig1, i + largura/2 - cX , altura/2 - cY , 0)
        desenha(fig1, janela)
        fig1 = transform.translate(fig1, -largura / 2 + cX, -altura/2 + cY, 0)
        #poligonos.imprime(fig1)
        poligonos.tamanho_aresta(fig1)
        time.sleep(.03)
        pygame.display.update()
        i+=10
        if(i>700):
            i = 0

main()