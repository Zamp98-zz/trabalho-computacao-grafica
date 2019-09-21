from cmath import sqrt

import numpy as np
import pygame

import poligonos

class Camera:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def projetaPoligono(poligono, janela):
    arestas = poligonos.get_arestas(poligono)

    cX = 2
    cY = poligono.centro[1]
    cZ = poligono.centro[2]
    r = -1/cX
    s = -1 / cY
    t = -1 / cZ

    matrizP = np.array([[1,0,0,0],
                        [0,1,0,0],
                        [0,0,1,0],
                        [r,s,t,1]])

    mP = np.array([[1,   0,      sqrt(2)/2,    0],
                   [0, 1, sqrt(2)/2, 0],
                   [0, 0,0,0],
                   [0, 0,0,1]])

    vertices = poligonos.get_vertices(poligono)
    temp = []
    for a in vertices:
        temp.append(a)

    temp = np.array(temp)

    R = np.dot(temp, matrizP)

    for i in range(len(R)):
        for j in range(len(R[i])):
            R[i][j] = R[i][j] / R[i][len(R[i])-1]

    #for i in range(len(R)):
    #    for j in range(len(R[0])):
    #        R[i][j] = R[i][j] / R[i][len(R[0])-1]

    print(R)

    for i in range(len(arestas)):
        pygame.draw.line(janela, (255, 255, 255),
                         (R[arestas[i][0]][0], R[arestas[i][0]][1]),
                         (R[arestas[i][1]][0], R[arestas[i][1]][1]), 1)
