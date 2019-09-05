import pygame
import poligonos


def desenha(figura, janela):
    arestas = poligonos.get_arestas(figura)
    vertices = poligonos.get_vertices(figura)
    pygame.draw.line(janela, (255,255,255), (arestas[0].a.x, arestas[0].a.y), (arestas[0].b.x, arestas[0].b.y),1)


def main():
    pygame.display.init()
    size = (600,400)
    janela = pygame.display.set_mode(size, 0, 0, 0)


    v1 = poligonos.Vertice(0, 0, 0)
    v2 = poligonos.Vertice(100, 200, 0)
    a = poligonos.Aresta(v1, v2)
    a.imprime()
    fig = poligonos.Poligono([v1, v2], [a])
    desenha(fig, janela)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        desenha(fig, janela)
        pygame.display.flip()


main()