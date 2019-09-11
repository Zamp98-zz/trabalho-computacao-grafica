from poligonos import get_vertices


vetTranX = [320, 0 , 0]

def quadroChaveTranX(figura):

    vertices = get_vertices(figura)
    #print(vertices)

    for i in range(len(vertices)):
        if(vertices[i][0] >= vetTranX[0]):
            return True

    return False
