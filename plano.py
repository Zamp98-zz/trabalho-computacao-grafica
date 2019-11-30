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

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):

    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)

    v1_n = np.sqrt(np.linalg.norm(v1_u))
    v2_n = np.sqrt(np.linalg.norm(v2_u))

    arcoss = np.arccos(np.dot(v1_u, v2_u) / np.dot(v1_n, v2_n))#Calcula o arcosseno

    return arcoss


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
        f = []
        for j in i:
            f.append([R[j][0], R[j][1]])

        res.append(f)

    vetores = []
    for i in faces:

        vet01 = []
        vet01.append(vertices[i[0]][0])
        vet01.append(vertices[i[0]][1])
        vet01.append(vertices[i[0]][2])
        vet02 = []
        vet02.append(vertices[i[1]][0])
        vet02.append(vertices[i[1]][1])
        vet02.append(vertices[i[1]][2])
        vet03 = []
        vet03.append(vertices[i[2]][0])
        vet03.append(vertices[i[2]][1])
        vet03.append(vertices[i[2]][2])

        vet = []
        vet.append(vet01)
        vet.append(vet02)
        vet.append(vet03)

        vetores.append(vet)# Pega os vetores ignorando a dimensão W

    for i in range(len(vetores)):
        vetores[i] = unit_vector(vetores[i])#Transforma os vetores em unitario

    normal = []
    for i in range(len(vetores)):
        normalTemp = np.cross(vetores[i][0], vetores[i][1])#Calcula a normal das faces
        normal.append(normalTemp)

    vetorluz = unit_vector([2, 5, 7])#Vetor que diz a direção da luz

    angulo = []
    for i in range(len(normal)):
        angulo.append(angle_between(normal[i], vetorluz))
        angulo[i] = angulo[i]*180/math.pi # Transforma radianos em graus

    i = 0
    for face in res:

        print(angulo[i])

        if(angulo[i] <= 90):
            cor = [168 - angulo[i], 168 - angulo[i], 168 - angulo[i]]
            pygame.draw.polygon(janela, cor, face)



        i += 1

