def mostrarPacientes(pilaPacientes):
      for paciente in pilaPacientes:
                print(f"Nombre: {paciente.nombre}, Apellido: {paciente.apellido}, Fecha de nacimiento: {paciente.fecha_nacimiento}, Edad: {paciente.edad}, Clasificación: {paciente.clasificacion}")