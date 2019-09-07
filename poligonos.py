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


