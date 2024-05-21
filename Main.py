from pacientes.paciente import Paciente
from pacientes.GestionDePacientes import GestionDePacientes
from datetime import date

def main():
    gestion_pacientes = GestionDePacientes()
    
    while True:
        print("Menú de opciones:")
        print("1. Leer pacientes")
        print("2. Agregar paciente")
        print("3. Actualizar paciente")
        print("4. Borrar paciente")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")
        if opcion == "1":
            # Leer pacientes
            print("Pacientes en la pila:")
            for paciente in gestion_pacientes.leer_pacientes():
                print(f"Nombre: {paciente.nombre}, Apellido: {paciente.apellido}, Fecha de nacimiento: {paciente.fecha_nacimiento}, Edad: {paciente.edad}, Clasificación: {paciente.clasificacion}")
        elif opcion == "2":
            # Agregar paciente
            nombre = input("Ingrese el nombre del paciente: ")
            apellido = input("Ingrese el apellido del paciente: ")
            tipo_documento = input("Ingrese el tipo de documento del paciente: ")
            documento_identidad = input("Ingrese el documento de identidad del paciente: ")
            while True:
                fecha_nacimiento_str = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
                try:
                    fecha_nacimiento = date.fromisoformat(fecha_nacimiento_str)
                    break
                except ValueError:
                    print("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato YYYY-MM-DD.")
            paciente = Paciente(nombre=nombre, apellido=apellido, tipo_documento=tipo_documento, documento_identidad=documento_identidad, fecha_nacimiento=fecha_nacimiento)
            gestion_pacientes.agregar_paciente(paciente)
        elif opcion == "3":
            # Actualizar paciente
            documento_identidad = input("Ingrese el documento de identidad del paciente que desea actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del paciente: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del paciente: ")
            if gestion_pacientes.actualizar_paciente(documento_identidad, nuevo_nombre, nuevo_apellido):
                print("Paciente actualizado correctamente.")
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")
        elif opcion == "4":
            # Borrar paciente
            documento_identidad = input("Ingrese el documento de identidad del paciente que desea borrar: ")
            if gestion_pacientes.borrar_paciente(documento_identidad):
                print("Paciente borrado correctamente.")
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")
        elif opcion == "5":
            # Salir
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()