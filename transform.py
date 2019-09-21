import math as m
import poligonos
import quadrosChave
import numpy as np

def shearing(figura, x, y, matriz):

    if(matriz == 1):
        S = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    elif(matriz == 2):
        S = np.array([
            [1, 0, 0, 0],
            [x, 1, 0, 0],
            [0, y, 1, 0],
            [0, 0, 0, 1]
        ])

    elif(matriz == 3):

        S = np.array([
            [1, y, 0, 0],
            [0, 1, 0, 0],
            [x, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    elif(matriz == 4):
        S = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [x, y, 1, 0],
            [0, 0, 0, 1]
        ])

    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)

    R = np.dot(B, S)

    fig = poligonos.Poligono(arestas, figura.centro)
    fig.addVertice(R)
    # print("\n", C, "\n")
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(figura.getDeslocamentoX())
    fig.setDeslocamentoY(figura.getDeslocamentoY())
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())

    return fig

def rotate(figura, x, y, z, fator):

    deslocamentoX = figura.getDeslocamentoX()
    deslocamentoY = figura.getDeslocamentoY()
    sentidoX = figura.getSentidoX()
    sentidoY = figura.getSentidoY()
    moveX = figura.getMoveX()
    moveY = figura.getMoveY()

    cos = m.cos(fator)
    sin = m.sin(fator)
    Rx = np.array([[1, 0, 0, 0],
                   [0, cos, -sin, 0],
                   [0, sin, cos, 0],
                   [0, 0, 0, 1]])

    Ry = np.array([[cos, 0, sin, 0],
                   [0, 1, 0, 0],
                   [-sin, 0, cos, 0],
                   [0, 0, 0, 1]])

    Rz = np.array([[cos, -sin, 0, 0],
                   [sin, cos, 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])
    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)
    if (x == 1):
        C = np.dot(B, Rx)
        figura = poligonos.Poligono(arestas, figura.centro)
        figura.addVertice(C)
    elif (y == 1):
        C = np.dot(B, Ry)
        figura = poligonos.Poligono(arestas, figura.centro)
        figura.addVertice(C)
    elif (z == 1):
        C = np.dot(B, Rz)
        figura = poligonos.Poligono(arestas, figura.centro)
        figura.addVertice(C)
    figura = poligonos.setCentro(figura)
    figura.setDeslocamentoX(deslocamentoX)
    figura.setDeslocamentoY(deslocamentoY)
    figura.setSentidoX(sentidoX)
    figura.setSentidoY(sentidoY)
    figura.setMoveX(moveX)
    figura.setMoveY(moveY)


    return figura

def scale(figura, fator):
    EX = EY = EZ = fator
    A = np.array([[EX, 0, 0, 0],
                  [0, EY, 0, 0],
                  [0, 0, EZ, 0],
                  [0, 0, 0, 1]])
    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)

    C = np.dot(B, A)

    fig = poligonos.Poligono(arestas, figura.centro)
    fig.addVertice(C)
    # print("\n", C, "\n")
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(figura.getDeslocamentoX())
    fig.setDeslocamentoY(figura.getDeslocamentoY())
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())

    return fig

def reflect(figura, qx, qy, qz):

    x = 1
    y = 1
    z = 1

    if(qx == True):
        y = -1
        z = -1
    if(qy == True):
        x = -1
        z = -1
    if(qz == True):
        x = -1
        y = -1

    A = np.array([[x, 0, 0, 0],
                   [0, y, 0, 0],
                   [0, 0, z, 0],
                   [0, 0, 0, 1]]
                  )
    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)

    C = np.dot(B, A)

    fig = poligonos.Poligono(arestas, figura.centro)
    fig.addVertice(C)
    # print("\n", C, "\n")
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(figura.getDeslocamentoX())
    fig.setDeslocamentoY(figura.getDeslocamentoY())
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())

    return fig

def translate(figura, x, y, z):

    deslocamentoX = figura.deslocamentoX()
    deslocamentoY = figura.deslocamentoY()

    if (quadrosChave.quadroChaveTransX(figura)):

        if(figura.getMoveY()):
            figura.setMoveY(False)
            figura.setSentidoY(False)
        else:
            figura.setMoveY(True)

        figura.inverteSentidoX()

    if (quadrosChave.quadroChaveTransY(figura)):
        #print(figura.getSentidoY)
        figura.inverteSentidoY()

    T = np.array([[1, 0, 0, x + deslocamentoX],
                  [0, 1, 0, y + deslocamentoY],
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
        linha = []
        for j in temp:
            linha.append(j[0])

        C.append(linha)
    fig = poligonos.Poligono(arestas, figura.centro)

    #print(fig.inverteX)
    fig.addVertice(C)
    # print("\n after translate:", C, "\n")
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(deslocamentoX)
    fig.setDeslocamentoY(deslocamentoY)
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())

    return fig
