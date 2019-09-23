import math as m
import numpy as np

centro = [0, 0, 0, 1]


class Aresta:
    def __init__(self, aresta):
        self.aresta = aresta

class Vertice:
    def __init__(self, vert):
        self.pontos = []
        for vertice in vert:
            self.pontos.append(vertice)

class Poligono:
    def __init__(self, arestas, centro):
        self.vertices = Vertice
        self.arestas = Aresta(arestas)
        self.verticeOriginal = Vertice
        self.centro = centro
        self.desX = 0
        self.desY = 0
        self.inverteX = False
        self.inverteY = False
        self.moveX = False
        self.moveY =False
        self.scale = 0

    def addVertice(self, vert):
        self.vertices = Vertice(vert)

    def addVerticeO(self, vert):
        self.verticeOriginal = Vertice(vert)

    def inverteSentidoX(self):
        if(self.inverteX):
            self.inverteX = False
        else:
            self.inverteX = True

    def inverteSentidoY(self):
        if(self.inverteY):
            self.inverteY = False
        else:
            self.inverteY = True

    def setSentidoX(self, sentido):
        self.inverteX = sentido

    def setSentidoY(self, sentido):
        self.inverteY = sentido

    def getSentidoX(self):
        return self.inverteX

    def getSentidoY(self):
        return self.inverteY

    def deslocamentoX(self):
        if(self.moveX):
            if(self.inverteX):
                self.desX -= 1.5
            else:
                self.desX += 1.5

        return self.desX

    def deslocamentoY(self):
        if(self.moveY):
            if(self.inverteY):
                self.desY += 1
            else:
                self.desY -= 1

        return self.desY

    def setDeslocamentoX(self, deslocamento):
        self.desX = deslocamento

    def setDeslocamentoY(self, deslocamento):
        self.desY = deslocamento

    def getDeslocamentoX(self):
        return self.desX

    def getDeslocamentoY(self):
        return self.desY

    def getCentro(self):
        return self.centro

    def setMoveX(self, moveX):
        self.moveX = moveX

    def setMoveY(self, moveY):
        self.moveY = moveY

    def getMoveX(self):
        return self.moveX

    def getMoveY(self):
        return self.moveY

    def setScale(self, scale):
        self.scale = scale

    def getScale(self):
        return self.scale

def setCentro(pol):
    centro = [0, 0, 0, 1]
    for v in pol.vertices.pontos:
        centro[0] += v[0]
        centro[1] += v[1]
        centro[2] += v[2]
    centro[0] = centro[0] / len(pol.vertices.pontos)
    centro[1] = centro[1] / len(pol.vertices.pontos)
    centro[2] = centro[2] / len(pol.vertices.pontos)

    pol.centro = centro
    return pol

def get_verticesO(pol):
    lista = []
    for vert in pol.verticeOriginal.pontos:
        lista.append(vert)
    return lista

def get_vertices(pol):
    lista = []
    for vert in pol.vertices.pontos:
        lista.append(vert)
    return lista


def get_arestas(pol):
    lista = []
    for ar in pol.arestas.aresta:
        lista.append(ar)
    return lista


def tamanho_aresta(pol):
    for aresta in pol.arestas:
        tX = pol.vertices[aresta[0]][0] - pol.vertices[aresta[1]][0]
        tY = pol.vertices[aresta[0]][1] - pol.vertices[aresta[1]][1]
        tZ = pol.vertices[aresta[0]][2] - pol.vertices[aresta[1]][2]
        H = m.sqrt(tX ** 2 + tY ** 2)
        tamanho = m.sqrt(H ** 2 + tZ ** 2)

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

    fig = Poligono([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11], [0, 0, 0, 1])
    fig.addVertice([v0, v1, v2, v3, v4, v5, v6, v7])
    return fig


#def imprime(figura):

#    for v in figura.vertices.vertice:

#    for a in figura.arestas.aresta:

#    centro = figura.centro

def get_zig():
    #primeira sequencia
    #da origem pra cima
    v0 = [0, 0, 0, 1]
    v1 = [3, 4, 0, 1]
    v2 = [0 , 8 , 0, 1]
    v3 = [3, 12, 0, 1]
    #segunda
    #do v3 pra baixo
    v4 = [3, 12, 3, 1]
    v5 = [0, 8, 3, 1]
    v6 = [3, 4, 3, 1]
    v7 = [0, 0, 3, 1]
    #terceira
    v8 = [3, 0, 0, 1]
    v9 = [6, 4, 0, 1]
    v10 = [3, 8, 0, 1]
    v11 = [6, 12, 0, 1]

    v12 = [6, 12, 3, 1]
    v13 = [3, 8, 3, 1]
    v14 = [6, 4, 3, 1]
    v15 = [3, 0, 3, 1]


    #g1
    a0 = [0, 1]
    a1 = [1, 2]
    a2 = [2, 3]
    a3 = [3, 4]
    a4 = [4, 5]
    a5 = [5, 6]
    a6 = [6, 7]
    a7 = [7, 0]
    #dobras da primeira parte
    a8 = [1, 6]
    a9 = [2, 5]
    #ligação entre g1 e g2
    a10 = [0, 8]
    a11 = [3, 11]
    #g2
    a12 = [8, 9]
    a13 = [9, 10]
    a14 = [10, 11]
    a15 = [11, 12]
    a16 = [12, 4]
    a17 = [12, 13]
    a18 = [13, 14]
    a19 = [14, 15]
    a20 = [15, 7]
    a21 = [15, 8]
    a22 = [9, 14]
    a23 = [10, 13]
    a24 = [10, 2]
    a25 = [13, 5]
    fig = Poligono([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25], [0, 0, 0, 1])
    fig.addVertice([v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15])
    fig.addVerticeO([v0, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15])
    return fig