import pygame
import plano
import poligonos
import quadrosChave
import transform


altura = 580
largura = 960

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
    pygame.display.set_caption("CARALHOW O EULLER É FODA!!!!")

    background = pygame.Surface(janela.get_size(), flags=pygame.SRCALPHA)
    background = background.convert_alpha()
    background.fill((0, 0, 0))

    fig1 = poligonos.get_cubo()
    fig1 = poligonos.setCentro(fig1)
    #fig1 = transform.shearing(fig1, 1, 1/2, 1)
    fig1.setMoveX(True)

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

        fig2 = transform.aumentaCisalhamento(fig2, janela, 2)
        fig2 = transform.diminuiCisalhamento(fig2, janela, 2)

        fig2 = transform.aumentaCisalhamento(fig2, janela, 3)
        fig2 = transform.diminuiCisalhamento(fig2, janela, 3)


main()