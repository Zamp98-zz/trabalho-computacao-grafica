import pygame

import plano
import poligonos
import transform


altura = 580
largura = 960

clock = pygame.time.Clock()

def main():
    pygame.display.init()
    size = (largura, altura)
    janela = pygame.display.set_mode(size, 0, 0, 0)

    pygame.display.set_caption("Computação Gráfica com um grupinho do barulho mais que bacana!!")

    background = pygame.Surface(janela.get_size(), flags=pygame.SRCALPHA)
    background = background.convert_alpha()
    background.fill((0, 0, 0))

    fig2 = poligonos.get_zig()
    fig2 = poligonos.setCentro(fig2)
    scale = 10
    fig2 = transform.scale(fig2, scale)

    inicio = True
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        scale = fig2.getScale()
        fig2 = transform.aumentaEscala(fig2, scale, janela, largura, altura) #Função para aumentar escala
        scale = fig2.getScale()
        fig2 = transform.diminuiEscala(fig2, scale, janela, largura, altura) #Função para reduzir escala

        #Só faz essa animação no inicio
        if(inicio == True):
            fig2 = transform.reflect(fig2, False, True, False)
            timeInicio = pygame.time.get_ticks()
            time = 0
            plano.projetaPoligono(fig2, janela)
            while (time - timeInicio < 800):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                cX1 = fig2.centro[0]
                cY1 = fig2.centro[1]
                cZ1 = fig2.centro[2]
                fig2 = transform.translate(fig2, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
                plano.projetaPoligono(fig2, janela)

                time = pygame.time.get_ticks()
                clock.tick(60)
                pygame.display.update()
                janela.fill((0, 0, 0, 1))

            fig2 = transform.reflect(fig2, True, False, False)
            timeInicio = pygame.time.get_ticks()
            time = 0
            plano.projetaPoligono(fig2, janela)
            while (time - timeInicio < 800):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                cX1 = fig2.centro[0]
                cY1 = fig2.centro[1]
                cZ1 = fig2.centro[2]
                fig2 = transform.translate(fig2, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
                plano.projetaPoligono(fig2, janela)

                time = pygame.time.get_ticks()
                clock.tick(60)
                pygame.display.update()
                janela.fill((0, 0, 0, 1))

            fig2 = transform.reflect(fig2, False, False, True)
            timeInicio = pygame.time.get_ticks()
            time = 0
            plano.projetaPoligono(fig2, janela)
            while (time - timeInicio < 800):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                cX1 = fig2.centro[0]
                cY1 = fig2.centro[1]
                cZ1 = fig2.centro[2]
                fig2 = transform.translate(fig2, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
                plano.projetaPoligono(fig2, janela)

                time = pygame.time.get_ticks()
                clock.tick(60)
                pygame.display.update()
                janela.fill((0, 0, 0, 1))

        fig2 = transform.transladaRotacionando(fig2, janela, largura, altura) #Função para mover e rotacionar a figura

        fig2 = transform.aumentaCisalhamento(fig2, janela, 1) #Função para aumentar o cisalhamento no eixo xy
        fig2 = transform.diminuiCisalhamento(fig2, janela, 1) #Função para diminuir o cisalhamento no eixo xy

        fig2 = transform.aumentaCisalhamento(fig2, janela, 2) #Função para aumentar o cisalhamento no eixo xz
        fig2 = transform.diminuiCisalhamento(fig2, janela, 2) #Função para diminuir o cisalhamento no eixo xz

        fig2 = transform.aumentaCisalhamento(fig2, janela, 3) #Função para aumentar o cisalhamento no eixo yz
        fig2 = transform.diminuiCisalhamento(fig2, janela, 3) #Função para diminuir o cisalhamento no eixo xz
        fig2 = transform.transladaRotacionando(fig2, janela, largura, altura)

        inicio = False

main()
