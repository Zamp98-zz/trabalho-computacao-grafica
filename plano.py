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


def projetaPoligonoWireframe(poligono, janela):

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
        pygame.draw.aaline(janela, (255, 255, 255),
                         (R[arestas[i][0]][0], R[arestas[i][0]][1]),
                         (R[arestas[i][1]][0], R[arestas[i][1]][1]), 1)


    #print("res:",res)

def projetaPoligonoFaces(poligono, janela):

    faces = poligonos.get_faces(poligono)
    cos = math.cos(3.14 / 4)
    sin = math.sin(3.14 / 4)

    matrizP = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [cos, sin, 0, 0],
                        [0, 0, 0, 1]])

    vertices = poligonos.get_vertices(poligono)
    temp = []
    for a in vertices:
        temp.append(a)

    temp = np.array(temp)

    R = np.dot(temp, matrizP)

    for i in range(len(R)):
        for j in range(len(R[i])):
            R[i][j] = R[i][j] / R[i][len(R[i]) - 1]

    res = []
    for i in faces:
        # print(i)
        f = []
        for j in i:
            # print(j, vertices[j][0], vertices[j][1])
            f.append([R[j][0], R[j][1]])
        res.append(f)

    cor = 20
    i = 0
    for face in res:
        #print(face)

        pygame.draw.polygon(janela, (cor + 10, cor + 15, cor + 20), face)

        #if(i!=11):
        #    pygame.draw.polygon(janela, (cor+10, cor+15, cor+20), face)
        #else:
        #    pygame.draw.polygon(janela, (cor + 10, cor + 15, cor + 20), face, -25)



        if(i < 9):
            cor += 10
            i += 1
        elif(i == 9):
            cor += 50
            i += 1
        elif(i == 10):
            cor -= 20
            i += 1


