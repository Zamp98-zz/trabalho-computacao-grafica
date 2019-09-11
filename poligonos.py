class Aresta:
    def __init__(self, inicio, fim):
        self.inicio = inicio
        self.fim = fim

class Poligono:
    def __init__(self, arestas):
        self.vertices = []
        self.arestas = arestas

    def addVertice(self, vert):
        for vertice in vert:
            self.vertices.append(vertice)

    '''def addAresta(self, ar):
        for (inicio, fim) in ar:
            self.arestas.append(Aresta(self.vertices[inicio], self.vertices[fim]))'''

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

def get_cubo():


    v0 = [0, 0, 0, 0]
    v1 = [0, 200, 0, 0]
    v2 = [200, 200, 0, 0]
    v3 = [200, 0, 0, 0]
    v4 = [50, 50, 250, 0]
    v5 = [250, 50, 250, 0]
    v6 = [250, 250, 250, 0]
    v7 = [50, 250, 250, 0]

    a0 = Aresta(v0, v1)
    a1 = Aresta(v0, v3)
    a2 = Aresta(v1, v2)
    a3 = Aresta(v2, v3)
    a4 = Aresta(v4, v5)
    a5 = Aresta(v4, v7)
    a6 = Aresta(v4, v0)
    a7 = Aresta(v5, v3)
    a8 = Aresta(v5, v6)
    a9 = Aresta(v6, v7)
    a10 = Aresta(v6, v2)
    a11 = Aresta(v7, v1)


    #a2.imprime()
    fig = Poligono([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11])
    fig.addVertice([v1, v2, v3, v4, v5, v6, v7])
    return fig
