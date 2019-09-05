
class Vertice:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def imprime(self):
        print(self.x, self.y, self. z)


class Aresta:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def imprime(self):
        print(self.a.imprime(), self.b.imprime())


class Poligono:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas


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