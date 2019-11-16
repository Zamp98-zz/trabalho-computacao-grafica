from poligonos import get_vertices

vetTrans = [[900, 500, 0],
            [100, 50, 0]]

def quadroChaveTransX(figura):
    centro = figura.getCentro()

    if (centro[0] >= vetTrans[0][0] and not figura.getSentidoX()):
        return True
    if (centro[0] <= vetTrans[1][0] and figura.getSentidoX()):
        return True

    return False

def quadroChaveTransY(figura):
    centro = figura.getCentro()

    if (centro[1] >= vetTrans[0][1] and  figura.getSentidoY()):
        return True
    if (centro[1] <= vetTrans[1][1] and not figura.getSentidoY()):
        return True

    return False

def quadroChaveCentro(figura, largura, altura):
    centro = figura.getCentro()

    if(int(centro[0]) == largura/2):
        return True


    return False

def quadroChaveScaleMax(figura, tam):

    if(figura.getScale() >= tam):
        return True

    return False

def quadroChaveScaleIdeal(figura, tam):

    if (figura.getScale() == tam):
        return True

    return False