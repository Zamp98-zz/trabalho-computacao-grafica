from cmath import sqrt

import numpy as np
import pygame

import poligonos
import math

class Camera:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def projetaPoligono(poligono, janela):
    arestas = poligonos.get_arestas(poligono)

    cos = math.cos(3.14/4)
    sin = math.sin(3.14/4)

    matrizP = np.array([[1,0,0,0],
                        [0,1,0,0],
                        [cos,sin,0,0],
                        [0,0,0,1]])

    vertices = poligonos.get_vertices(poligono)
    temp = []
    for a in vertices:
        temp.append(a)

    temp = np.array(temp)

    R = np.dot(temp, matrizP)

    for i in range(len(R)):
        for j in range(len(R[i])):
            R[i][j] = R[i][j] / R[i][len(R[i])-1]

    for i in range(len(arestas)):
        pygame.draw.line(janela, (255, 255, 255),
                         (R[arestas[i][0]][0], R[arestas[i][0]][1]),
                         (R[arestas[i][1]][0], R[arestas[i][1]][1]), 1)

