import math
import poligonos
import quadrosChave

xcp = -5
zcp = -5
ycp = -5
matrizCP = (
    (1,0,0, -1/xcp),
    (0, 1, 0, -1/ycp),
    (0, 0, 1, -1/zcp),
    (0, 0, 0, 1)
)


matrizP = (
    (math.cos(3.14), math.sin(3.14) * math.sin(3.14), 0, 0),
    (0, math.cos(3.14), 0, 0),
    (math.sin(3.14), 0, -math.sin(3.14) * math.cos(3.14), 0),
    (0, 0, 0, 1)
)

transX = [20, 0, 0]
transY = [0, 20, 0]
transZ = [0, 0, 1]


def translate(figura, eixo, d, ar):

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
        print(transX[0])
    #if (quadrosChave.quadroChaveTranY(figura)):
    #    transX[1] *= -1
    #if (quadrosChave.quadroChaveTranZ(figura)):
    #    transX[2] *= -1
    fig.addVertice(vertice)
    return fig