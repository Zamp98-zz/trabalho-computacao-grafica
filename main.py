import pygame
import os
import plano
import poligonos
import transform

import time

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
        pygame.draw.line(janela, (255, 255, 255),
                           (figura.vertices.vertice[arestas[i][0]][0], figura.vertices.vertice[arestas[i][0]][1]),
                           (figura.vertices.vertice[arestas[i][1]][0], figura.vertices.vertice[arestas[i][1]][1]),1)


clock = pygame.time.Clock()

def main():
    pygame.display.init()
    size = (largura, altura)
    janela = pygame.display.set_mode(size, 0, 0, 0)
    pygame.display.set_caption("Computação Gráfica com um grupinho do barulho mais que bacana!!")
    pygame.display.set_caption("Ei você, vai se fudê!!")
    pygame.display.set_caption("Zamp#")
    pygame.display.set_caption("ComPutaSão Gráfica")

    background = pygame.Surface(janela.get_size(), flags=pygame.SRCALPHA)
    background = background.convert_alpha()
    background.fill((0, 0, 0))

    fig1 = poligonos.get_cubo()
    fig1 = poligonos.setCentro(fig1)
    #fig1 = transform.shearing(fig1, 1, 1/2, 1)
    fig1.setMoveX(True)

    fig2 = poligonos.get_zig()
    fig2 = poligonos.setCentro(fig2)
    fig2 = transform.scale(fig2, 20)

    time = 1/ pygame.time.get_ticks()

    while True:
        print(time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        fig1 = transform.rotate(fig1, 1, 0, 0, 1 / 200)
        fig1 = transform.rotate(fig1, 0, 1, 0, 1 / 200)
        fig1 = transform.rotate(fig1, 0, 0, 1, 1 / 200)
        cX = fig1.centro[0]
        cY = fig1.centro[1]
        cZ = fig1.centro[2]
        # fig1 = transform.reflect(fig1, True, True, False)
        fig1 = transform.translate(fig1, largura / 2 - cX, altura / 2 - cY, -cZ)
        plano.projetaPoligono(fig1, janela)

        fig2 = transform.rotate(fig2, 1, 0, 0, 1/200)
        fig2 = transform.rotate(fig2, 0, 1, 0, 1 / 200)
        fig2 = transform.rotate(fig2, 0, 0, 1, 1 / 200)
        cX1 = fig2.centro[0]
        cY1 = fig2.centro[1]
        cZ1 = fig2.centro[2]
        fig2 = transform.translate(fig2, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
        plano.projetaPoligono(fig2, janela)

        clock.tick(10)
        pygame.display.update()
        janela.fill((0, 0, 0, 1))

main()