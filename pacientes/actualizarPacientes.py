
def actualizarDatos(pila, documento):
    while True:
        print ("Actualización de datos")
        print("------------------------")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Tipo de documento")
        print("4. Documento")
        print("5. Fecha de nacimiento")
        print("6. Salir")
        opcion = input("Elija un campo para editar: ")
        
        if opcion == "1":
            #Actualizar nombre
            nuevoNombre = input("Ingrese el nombre: ")
            pila.actualizar_paciente(documento, "nombre", nuevoNombre)

        elif opcion == "2":
            #Actualizar apellido
            nuevoApellido = input("Ingrese el apellido: ")
            pila.actualizar_paciente(documento, "apellido", nuevoApellido)

        elif opcion == "3":
            #Actualizar tipo de documento
            nuevoTipo = input("Ingrese el tipo de documento (CC/TI/DIG): ")
            pila.actualizar_paciente(documento, "tipo_documento", nuevoTipo)

        elif opcion == "4":
            #Actualizar documento
            nuevoDocumento = input("Ingrese el nuevo número de documento: ")
            pila.actualizar_paciente(documento, "documento_identidad", nuevoDocumento)

        elif opcion == "5":
            #Actualizar fecha de nacimiento
            nuevaFecha = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
            pila.actualizar_paciente(documento, "fecha_nacimiento", nuevaFecha)

        elif opcion == "6":
            print("Saliendo de Actualización de Datos...")
            break
        
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

        
        