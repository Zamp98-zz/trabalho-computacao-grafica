import math as m
import pygame
import poligonos
import quadrosChave
import numpy as np
import plano

clock = pygame.time.Clock()

def transladaParaOrigem(vertices, escolha, centro):


    if(escolha):

        T = np.array([[1, 0, 0, -centro[0]],
                      [0, 1, 0, -centro[1]],
                      [0, 0, 1, -centro[2]],
                      [0, 0, 0, 1]])

    else:
        T = np.array([[1, 0, 0, centro[0]],
                      [0, 1, 0, centro[1]],
                      [0, 0, 1, centro[2]],
                      [0, 0, 0, 1]])

    temp = []
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

    return C

def shearing(figura, x, y, z, matriz):

    if(matriz == 1):
        S = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [x, y, 1, 0],
            [0, 0, 0, 1]
        ])

    elif(matriz == 2):
        S = np.array([
            [1, 0, 0, 0],
            [x, 1, z, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    elif(matriz == 3):

        S = np.array([
            [1, y, z, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    else:#Caso não digite nada multiplica pela identidade.
        S = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

    vertices = poligonos.get_vertices(figura)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)

    R = np.dot(B, S)

    fig = poligonos.Poligono(arestas, figura.centro, figura.faces)
    fig.addVertice(R)
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(figura.getDeslocamentoX())
    fig.setDeslocamentoY(figura.getDeslocamentoY())
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())
    fig.setScale(figura.getScale())

    return fig

def rotate(figura, x, y, z, fator):

    deslocamentoX = figura.getDeslocamentoX()
    deslocamentoY = figura.getDeslocamentoY()
    sentidoX = figura.getSentidoX()
    sentidoY = figura.getSentidoY()
    moveX = figura.getMoveX()
    moveY = figura.getMoveY()
    scale = figura.getScale()

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
        figura = poligonos.Poligono(arestas, figura.centro, figura.faces)
        figura.addVertice(C)
        figura.addVerticeO(C)
    elif (y == 1):
        C = np.dot(B, Ry)
        figura = poligonos.Poligono(arestas, figura.centro, figura.faces)
        figura.addVertice(C)
        figura.addVerticeO(C)
    elif (z == 1):
        C = np.dot(B, Rz)
        figura = poligonos.Poligono(arestas, figura.centro, figura.faces)
        figura.addVertice(C)
        figura.addVerticeO(C)

    figura = poligonos.setCentro(figura)
    figura.setDeslocamentoX(deslocamentoX)
    figura.setDeslocamentoY(deslocamentoY)
    figura.setSentidoX(sentidoX)
    figura.setSentidoY(sentidoY)
    figura.setMoveX(moveX)
    figura.setMoveY(moveY)
    figura.setScale(scale)


    return figura

def scale(figura, fator):

    if(figura.getScale() != 0):
        aux = figura.getScale()
        figura.setScale(0)
        figura = scale(figura, 1/aux)

    EX = EY = EZ = fator
    A = np.array([[EX, 0, 0, 0],
                  [0, EY, 0, 0],
                  [0, 0, EZ, 0],
                  [0, 0, 0, 1]])

    vertices = poligonos.get_vertices(figura)

    centro = figura.getCentro()

    vertices = transladaParaOrigem(vertices, True, centro)
    temp = []
    arestas = poligonos.get_arestas(figura)
    for a in vertices:
        temp.append(a)
    B = np.array(temp)

    C = np.dot(B, A)

    C = transladaParaOrigem(C, False, centro)

    fig = poligonos.Poligono(arestas, figura.centro, figura.faces)
    fig.addVertice(C)
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(figura.getDeslocamentoX())
    fig.setDeslocamentoY(figura.getDeslocamentoY())
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())
    fig.setScale(fator)

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

    fig = poligonos.Poligono(arestas, figura.centro, figura.faces)
    fig.addVertice(C)
    fig.addVerticeO(C)
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(figura.getDeslocamentoX())
    fig.setDeslocamentoY(figura.getDeslocamentoY())
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())
    fig.setScale(figura.getScale())

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
    fig = poligonos.Poligono(arestas, figura.centro, figura.faces)

    fig.addVertice(C)
    fig.addVerticeO(C)
    fig = poligonos.setCentro(fig)
    fig.setDeslocamentoX(deslocamentoX)
    fig.setDeslocamentoY(deslocamentoY)
    fig.setSentidoX(figura.getSentidoX())
    fig.setSentidoY(figura.getSentidoY())
    fig.setMoveX(figura.getMoveX())
    fig.setMoveY(figura.getMoveY())
    fig.setScale(figura.getScale())

    return fig

def aumentaEscala(figura, scaleVar, janela, largura, altura):

    timeInicio = pygame.time.get_ticks()
    time = pygame.time.get_ticks()
    while (time - timeInicio < 2000):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        scaleVar += 0.05

        figura = poligonos.setCentro(figura)
        figura = scale(figura, scaleVar)

        cX1 = figura.centro[0]
        cY1 = figura.centro[1]
        cZ1 = figura.centro[2]
        figura = translate(figura, largura / 2 - cX1 , altura / 2 - cY1 , -cZ1)

        plano.projetaPoligonoFaces(figura, janela)

        time = pygame.time.get_ticks()
        clock.tick(60)
        pygame.display.update()
        janela.fill((0, 0, 0, 1))


    return figura

def diminuiEscala(figura, scaleVar, janela, largura, altura):
    timeInicio = pygame.time.get_ticks()
    time = pygame.time.get_ticks()
    while (time - timeInicio < 2000):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        scaleVar -= 0.05

        figura = poligonos.setCentro(figura)
        figura = scale(figura, scaleVar)

        cX1 = figura.centro[0]
        cY1 = figura.centro[1]
        cZ1 = figura.centro[2]
        figura = translate(figura, largura / 2 - cX1, altura / 2 - cY1, -cZ1)

        plano.projetaPoligonoFaces(figura, janela)

        time = pygame.time.get_ticks()
        clock.tick(60)
        pygame.display.update()
        janela.fill((0, 0, 0, 1))

    return figura

def aumentaCisalhamento(figura, janela, x):

    timeInicio = pygame.time.get_ticks()
    time = pygame.time.get_ticks()

    while (time - timeInicio < 4000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        time = pygame.time.get_ticks()

        figura = shearing(figura, 0.001, 0.001, 0.001, x)
        plano.projetaPoligonoWireframe(figura, janela)

        clock.tick(60)
        pygame.display.update()
        janela.fill((0, 0, 0, 1))


    return figura


def diminuiCisalhamento(figura, janela, x):

    timeInicio = pygame.time.get_ticks()
    time = pygame.time.get_ticks()

    while (time - timeInicio < 4000):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        time = pygame.time.get_ticks()

        figura = shearing(figura, -0.001, -0.001, -0.001, x)
        plano.projetaPoligonoWireframe(figura, janela)

        clock.tick(60)
        pygame.display.update()
        janela.fill((0, 0, 0, 1))

    return figura


def transladaRotacionando(figura, janela, largura, altura):

    cX1 = figura.centro[0]
    cY1 = figura.centro[1]
    cZ1 = figura.centro[2]
    figura.setMoveX(True)
    figura = translate(figura, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
    plano.projetaPoligonoWireframe(figura, janela)

    while (not quadrosChave.quadroChaveCentro(figura, largura, altura)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        cX1 = figura.centro[0]
        cY1 = figura.centro[1]
        cZ1 = figura.centro[2]
        figura = translate(figura, largura / 2 - cX1, altura / 2 - cY1, -cZ1)
        figura = rotate(figura, 1, 0, 0, 1 / 100)
        figura = rotate(figura, 0, 1, 0, 1 / 100)
        figura = rotate(figura, 0, 0, 1, 1 / 100)
        plano.projetaPoligonoWireframe(figura, janela)

        clock.tick(60)
        pygame.display.update()
        janela.fill((0, 0, 0, 1))

    figura.setMoveY(False)
    figura.setMoveX(False)

    return figura