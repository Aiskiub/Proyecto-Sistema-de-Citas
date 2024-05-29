def busquedaBinaria(array, min, max, x, atributo):

    while min <= max:
        mitad = min + (max - min) // 2
        # Revisa si x se encuentra en la mitad
        if int(getattr(array[mitad],atributo)) == x:
            return array[mitad]

        # Si x es mayor, ignorar la mitad izquierda
        elif int(getattr(array[mitad], atributo)) < x:
            min = mitad + 1

        # Si x es menor, ignorar la mitad derecha
        else:
            max = mitad - 1

    # Si se llega hasta acá, es porque no se halló a x
    return -1