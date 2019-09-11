import math as m
import poligonos
import quadrosChave
import numpy as np

transX = [20, 0, 0]
transY = [0, 20, 0]
transZ = [0, 0, 1]


def rotate(figura, x, y, z, fator):
    cos = m.cos(m.pi*fator)
    sin = m.sin(m.pi*fator)
    Rx = np.array([[1,  0,    0,  0],
                   [0, cos, -sin, 0],
                   [0, sin, cos,  0],
                   [0,   0,  0,   1]])

    Ry = np.array([[cos, 0, sin, 0],
                   [0,   1,  0,  0],
                   [-sin, 0, cos, 0],
                   [  0,  0,  0,  1]])

    Rz = np.array([[cos, -sin, 0, 0],
                   [sin, cos,  0, 0],
                   [0,    0,   1, 0],
                   [0,    0,   0, 1]])
    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)
    fig = figura
    if(x == 1):
        C = np.dot(B, Rx)
        figura = poligonos.Poligono(arestas)
        figura.addVertice(C)
    elif(y == 1):
        C = np.dot(B, Ry)
        figura = poligonos.Poligono(arestas)
        figura.addVertice(C)
    elif(z == 1):
        C = np.dot(figura.vertices, Rz)
        figura = poligonos.Poligono(arestas)
        figura.addVertice(C)
    figura = poligonos.setCentro(figura)
    return figura

def scale(figura, fator):
    EX = EY = EZ = fator
    A = np.array([[EX, 0, 0, 0],
                  [0, EY, 0, 0],
                  [0, 0, EZ, 0],
                  [0, 0, 0, 0]])
    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)

    C = np.dot(B, A)

    fig = poligonos.Poligono(arestas)
    fig.addVertice(C)
    #print("\n", C, "\n")
    fig = poligonos.setCentro(fig)
    return fig

def translate(figura, x, y, z):
    T = np.array([[1, 0, 0, x],
                  [0, 1, 0, y],
                  [0, 0, 1, z],
                  [0, 0, 0, 1]])
    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)

    C = []
    for i in B:
        temp = np.dot(T, [
            [i[0]],
            [i[1]],
            [i[2]],
            [i[3]]])
        linha=[]
        for j in temp:
            linha.append(j[0])

        C.append(linha)
    fig = poligonos.Poligono(arestas)
    fig.addVertice(C)
    print("\n after translate:", C, "\n")
    return fig


'''def translate(figura, eixo, d, ar):

    vertice = poligonos.get_vertices(figura)
    fig = poligonos.Poligono(ar)

    if(eixo == 'x'):
        for i in range(len(vertice)):
            vertice[i][0] += transX[0] + d
    elif (eixo == 'y'):
        for i in range(len(vertice)):
            vertice[i][1] += transY[1] + d
    elif (eixo == 'z'):
        for i in range(len(vertice)):
            vertice[i][2] += transY[2] + d

    if(quadrosChave.quadroChaveTranX(figura) and transX[0] == 20):
        transX[0] *= -1
        #print(transX[0])
    #if (quadrosChave.quadroChaveTranY(figura)):
    #    transX[1] *= -1
    #if (quadrosChave.quadroChaveTranZ(figura)):
    #    transX[2] *= -1
    fig.addVertice(vertice)
    return fig'''''