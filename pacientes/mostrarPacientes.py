def mostrarPacientes(pilaPacientes):
    for paciente in pilaPacientes:
        print(f"Nombre: {paciente.nombre}, Apellido: {paciente.apellido},"
            f"Documento: {paciente.documento_identidad},"
            f"Fecha de nacimiento: {paciente.fecha_nacimiento}, Edad: {paciente.edad},"
            f"Clasificación: {paciente.clasificacion}")