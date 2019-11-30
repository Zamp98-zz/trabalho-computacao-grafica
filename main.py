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

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        scale = fig2.getScale()
        fig2 = transform.aumentaEscala(fig2, scale, janela, largura, altura) #Função para aumentar escala
        scale = fig2.getScale()
        fig2 = transform.diminuiEscala(fig2, scale, janela, largura, altura) #Função para reduzir escala


        fig3 = poligonos.calcula_figura_curva(fig2) #Cria uma figura com curvas
        fig3 = poligonos.setCentro(fig3)
        fig3 = transform.reflect(fig3, False, True, False) #Faz a figura refletir no eixo Y
        timeInicio = pygame.time.get_ticks()
        time = 0
        plano.projetaPoligonoWireframe(fig3, janela)
        while (time - timeInicio < 800): #Exibe a imagem da figura refletida por um tempo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            cX1 = fig3.centro[0]
            cY1 = fig3.centro[1]
            cZ1 = fig3.centro[2]
            fig3 = transform.translate(fig3, largura / 2 - cX1, altura / 2 - cY1, -cZ1)

            plano.projetaPoligonoWireframe(fig3, janela)
            time = pygame.time.get_ticks()
            clock.tick(60)
            pygame.display.update()
            janela.fill((0, 0, 0, 1))

        fig3 = transform.reflect(fig3, True, False, False)#Faz a figura refletir no eixo X
        timeInicio = pygame.time.get_ticks()
        time = 0
        plano.projetaPoligonoWireframe(fig3, janela)
        while (time - timeInicio < 800):#Exibe a imagem da figura refletida por um tempo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            cX1 = fig3.centro[0]
            cY1 = fig3.centro[1]
            cZ1 = fig3.centro[2]
            fig3 = transform.translate(fig3, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
            plano.projetaPoligonoWireframe(fig3, janela)

            time = pygame.time.get_ticks()
            clock.tick(60)
            pygame.display.update()
            janela.fill((0, 0, 0, 1))

        fig3 = transform.reflect(fig3, False, False, True)#Faz a figura refletir no eixo Z
        timeInicio = pygame.time.get_ticks()
        time = 0
        plano.projetaPoligonoWireframe(fig3, janela)
        while (time - timeInicio < 800):#Exibe a imagem da figura refletida por um tempo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            cX1 = fig3.centro[0]
            cY1 = fig3.centro[1]
            cZ1 = fig3.centro[2]
            fig3 = transform.translate(fig3, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
            plano.projetaPoligonoWireframe(fig3, janela)

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