import pygame
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
    pygame.display.set_caption("Ei você, vai se fudê!!")
    pygame.display.set_caption("Zamp#")
    pygame.display.set_caption("ComPutaSão Gráfica")
    pygame.display.set_caption("CARALHOW O EULLER É FODA!!!!")

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
        fig2 = transform.aumentaEscala(fig2, scale, janela, largura, altura)
        scale = fig2.getScale()
        fig2 = transform.diminuiEscala(fig2, scale, janela, largura, altura)
        fig2 = transform.transladaRotacionando(fig2, janela, largura, altura)

        fig2 = transform.aumentaCisalhamento(fig2, janela, 1)
        fig2 = transform.diminuiCisalhamento(fig2, janela, 1)
        fig2 = transform.transladaRotacionando(fig2, janela, largura, altura)

        fig2 = transform.aumentaCisalhamento(fig2, janela, 2)
        fig2 = transform.diminuiCisalhamento(fig2, janela, 2)
        fig2 = transform.transladaRotacionando(fig2, janela, largura, altura)

        fig2 = transform.aumentaCisalhamento(fig2, janela, 3)
        fig2 = transform.diminuiCisalhamento(fig2, janela, 3)
        fig2 = transform.transladaRotacionando(fig2, janela, largura, altura)


main()