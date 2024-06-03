from datetime import datetime, date
from utils.logger import Logger as log

def actualizarDatos(pila, paciente):
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
            pila.actualizar_paciente(paciente, "nombre", nuevoNombre)

        elif opcion == "2":
            #Actualizar apellido
            nuevoApellido = input("Ingrese el apellido: ")
            pila.actualizar_paciente(paciente, "apellido", nuevoApellido)

        elif opcion == "3":
            #Actualizar tipo de documento
            nuevoTipo = input("Ingrese el tipo de documento (CC/TI/DIG): ")
            pila.actualizar_paciente(paciente, "tipo_documento", nuevoTipo)

        elif opcion == "4":
            #Actualizar documento
            nuevoDocumento = input("Ingrese el nuevo número de documento: ")
            pila.actualizar_paciente(paciente, "documento_identidad", nuevoDocumento)

        elif opcion == "5":
            while True:
                fecha_nacimiento_str = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
                try:
                    fecha_nacimiento = date.fromisoformat(fecha_nacimiento_str)
                    break
                except ValueError:
                    log.error("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato YYYY-MM-DD.")
            pila.actualizar_paciente(paciente, "fecha_nacimiento", fecha_nacimiento)

        elif opcion == "6":
            print("Saliendo de Actualización de Datos...")
            break
        
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
