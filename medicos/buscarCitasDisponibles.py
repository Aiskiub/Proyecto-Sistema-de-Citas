def buscarCitasDisponibles(medico, fecha):
    try:
        mallaMedico = medico.citas
        print("Horarios disponibles en la fecha " + fecha + ": ")
        dictFecha = mallaMedico[fecha]
        citas_disponibles = False
        for key in dictFecha:
            print("////")
            if dictFecha[key] == 'true':
                print(key + " - Disponible")
                citas_disponibles = True
        return citas_disponibles
    except:
        print("No hay citas en la fecha que indico, ingrese una fecha dentro de 30 dias a partir de hoy")
        return False
