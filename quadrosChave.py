from poligonos import get_vertices

vetTrans = [[1150, 500, 0],
            [150, 80, 0]]

def quadroChaveTransX(figura):
    centro = figura.getCentro()
    # print(vertices)

    if (centro[0] >= vetTrans[0][0] and not figura.getSentidoX()):
        return True
    if (centro[0] <= vetTrans[1][0] and figura.getSentidoX()):
        return True

    return False

def quadroChaveTransY(figura):
    centro = figura.getCentro()
    # print(vertices)
    if (centro[1] >= vetTrans[0][1] and figura.getSentidoY()):
        return True
    if (centro[1] <= vetTrans[1][1] and not figura.getSentidoY()):
        return True

    return False
