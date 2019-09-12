import math as m

centro = [0, 0, 0, 1]
class Poligono:
    def __init__(self, arestas, centro):
        self.vertices = []
        self.arestas = arestas
        self.centro = centro
    def addVertice(self, vert):
        for vertice in vert:
            self.vertices.append(vertice)

    '''def addAresta(self, ar):
        for (inicio, fim) in ar:
            self.arestas.append(Aresta(self.vertices[inicio], self.vertices[fim]))'''


def setCentro(pol):
    centro = [0, 0, 0, 1]
    for v in pol.vertices:
        centro[0] += v[0]
        centro[1] += v[1]
        centro[2] += v[2]
    centro[0] = centro[0] / len(pol.vertices)
    centro[1] = centro[1] / len(pol.vertices)
    centro[2] = centro[2] / len(pol.vertices)
    print("Set centro:",centro)
    pol.centro = centro
    return pol


def get_vertices(pol):
    lista = []
    for vert in pol.vertices:
        lista.append(vert)
    return lista


def get_arestas(pol):
    lista = []
    for ar in pol.arestas:
        lista.append(ar)
    return lista


def tamanho_aresta(pol):
    for aresta in pol.arestas:
        tX = pol.vertices[aresta[0]][0] - pol.vertices[aresta[1]][0]
        tY = pol.vertices[aresta[0]][1] - pol.vertices[aresta[1]][1]
        tZ = pol.vertices[aresta[0]][2] - pol.vertices[aresta[1]][2]
        H = m.sqrt(tX ** 2 + tY ** 2)
        tamanho = m.sqrt(H ** 2 + tZ ** 2)
        # print("tamanho das arestas:", round(tamanho, 0))
        return int(round(tamanho, 0))


def get_cubo():
    v0 = [0, 0, 0, 1]
    v1 = [0, 200, 0, 1]
    v2 = [200, 200, 0, 1]
    v3 = [200, 0, 0, 1]
    v4 = [0, 0, 200, 1]
    v5 = [200, 0, 200, 1]
    v6 = [200, 200, 200, 1]
    v7 = [0, 200, 200, 1]

    a0 = [0, 1]
    a1 = [0, 3]
    a2 = [1, 2]
    a3 = [2, 3]
    a4 = [4, 5]
    a5 = [4, 7]
    a6 = [4, 0]
    a7 = [5, 3]
    a8 = [5, 6]
    a9 = [6, 7]
    a10 = [6, 2]
    a11 = [7, 1]

    # a2.imprime()
    fig = Poligono([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11], [0, 0, 0, 1])
    fig.addVertice([v0, v1, v2, v3, v4, v5, v6, v7])
    return fig


def imprime(figura):
    # print("imprime figura:")
    for v in figura.vertices:
        print("Vertices:",v)
    for a in figura.arestas:
        print("Arestas:",a)
    centro = figura.centro
    print("Centro:", centro)
