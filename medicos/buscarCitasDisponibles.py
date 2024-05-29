def buscarCitasDisponibles(medico, fecha):

        try:
            mallaMedico = medico.citas
            print("Horarios disponibles en la fecha " + fecha + ": ")
            dictFecha = mallaMedico[fecha]
            for key in dictFecha:
             if dictFecha[key] == 'true':
                print(key)
            return
        except:
         print("No hay citas en la fecha que indico, ingrese una fecha dentro de 30 dias a partir de hoy")
         return