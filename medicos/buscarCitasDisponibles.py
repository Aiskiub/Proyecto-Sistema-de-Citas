def buscarCitasDisponibles(medico, fecha):
    try:
        mallaMedico = medico.citas
        print("Horarios disponibles en la fecha " + fecha + ": ")
        # Obtener el diccionario de horarios para la fecha especificada
        dictFecha = mallaMedico[fecha]
        # Inicializar una bandera para verificar si hay citas disponibles
        citas_disponibles = False
        # Iterar sobre los horarios en el diccionario de la fecha
        for key in dictFecha:
            print("////")
            # Si el valor del horario es 'true', significa que está disponible
            if dictFecha[key] == 'true':
                # Imprimir el horario disponible
                print(key + " - Disponible")
                # Marcar que hay al menos una cita disponible
                citas_disponibles = True
        # Devolver el resultado de si hay citas disponibles o no
        return citas_disponibles
    except KeyError:
        # Manejar el caso en que la fecha no esté en la malla de citas del médico, por si se pasa de los 30 dias
        print("No hay citas en la fecha que indicó, ingrese una fecha dentro de 30 días a partir de hoy")
        return False
