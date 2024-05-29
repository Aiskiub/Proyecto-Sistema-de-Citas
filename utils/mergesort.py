def mergeSort(array, indiceIzq, indiceDer, criterioComparacion):
    if indiceIzq >= indiceDer:
        return

    mitad = (indiceIzq + indiceDer)//2
    mergeSort(array, indiceIzq, mitad, criterioComparacion)
    mergeSort(array, mitad + 1, indiceDer, criterioComparacion)
    merge(array, indiceIzq, indiceDer, mitad, criterioComparacion)

def merge(array, indiceIzq, indiceDer, mitad, criterioComparacion):
    #Copias de ambos lados del array
    copiaIzq = array[indiceIzq:mitad + 1]
    copiaDer = array[mitad+1:indiceDer+1]
    #Inicializamos indices
    indiceCopiaIzq = 0
    indiceCopiaDer = 0
    indiceOrdenado = indiceIzq

    # Recorrer ambas copias hasta que alguna de ellas se agote
    while indiceCopiaIzq < len(copiaIzq) and indiceCopiaDer < len(copiaDer):
        # Si copiaIzq tiene el elemento más pequeño, añadir a la parte ordenada
        # y aumentar el índice izquierdo en uno
        if criterioComparacion(copiaIzq[indiceCopiaIzq], copiaDer[indiceCopiaDer]):
            array[indiceOrdenado] = copiaIzq[indiceCopiaIzq]
            indiceCopiaIzq = indiceCopiaIzq + 1
        # Lo contrario a lo de arriba
        else:
            array[indiceOrdenado] = copiaDer[indiceCopiaDer]
            indiceCopiaDer = indiceCopiaDer + 1

        # Avanzar indice de la parte ordenada
        indiceOrdenado = indiceOrdenado + 1

    # Una vez agotados los elementos de la izquierda o derecha, añadir los sobrantes:
    while indiceCopiaIzq < len(copiaIzq):
        array[indiceOrdenado] = copiaIzq[indiceCopiaIzq]
        indiceCopiaIzq = indiceCopiaIzq + 1
        indiceOrdenado = indiceOrdenado + 1

    while indiceCopiaDer < len(copiaDer):
        array[indiceOrdenado] = copiaDer[indiceCopiaDer]
        indiceCopiaDer = indiceCopiaDer + 1
        indiceOrdenado = indiceOrdenado + 1
    