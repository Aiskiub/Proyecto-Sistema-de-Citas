import pandas as pd
from medicos.medico import Medico
from pacientes.paciente import Paciente
from pacientes.GestionDePacientes import GestionDePacientes
from citas.GestionDeCitas import GestionDeCitas
from datetime import date, datetime, time
from medicos.GestionDeMedicos import GestionDeMedicos
import os


def main():

    # Aquí se crean instancias de Gestión de Pacientes y Gestión de Citas
    gestion_pacientes = GestionDePacientes()
    gestion_medico = GestionDeMedicos()

    # Ruta absoluta al archivo Excel
    ruta_excel_medicos = 'C:/Users/ASUS/OneDrive/Documentos/Proyecto Estructura/Proyecto-Sistema-de-Citas/excel/archivo.xlsx'
    ruta_excel_pacientes = 'C:/Users/ASUS/OneDrive/Documentos/Proyecto Estructura/Proyecto-Sistema-de-Citas/excel/pacientes.xlsx'
    
    # Verificar si los archivos existen
    if not os.path.exists(ruta_excel_medicos):
        print(f"El archivo de médicos no existe: {ruta_excel_medicos}")
        return

    if not os.path.exists(ruta_excel_pacientes):
        print(f"El archivo de pacientes no existe: {ruta_excel_pacientes}")
        return

    # Cargar datos de médicos desde el archivo Excel
    gestion_medico.cargar_medicos_desde_excel(ruta_excel_medicos)

    # Crear instancia de GestionDeCitas y pasarle la instancia de GestionDeMedicos
    gestion_citas = GestionDeCitas(gestion_medico)

    # Cargar datos de pacientes desde el archivo Excel
    gestion_pacientes.cargar_pacientes_desde_excel(ruta_excel_pacientes)

    while True:
        print("Menú de opciones:")
        print("1. Leer pacientes")
        print("2. Agregar paciente")
        print("3. Actualizar paciente")
        print("4. Borrar paciente")
        print("5. Asignar cita")
        print("6. Cancelar cita")
        print("7. Mostrar citas")
        print("8. Ver médicos disponibles")
        print("9. Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            # Leer pacientes
            print("Pacientes en la pila:")
            for paciente in gestion_pacientes.leer_pacientes():
                print(f"Nombre: {paciente.nombre}, Apellido: {paciente.apellido}, Fecha de nacimiento: {paciente.fecha_nacimiento}, Edad: {paciente.edad}, Clasificación: {paciente.clasificacion}")
        elif opcion == "2":
            # Agregar paciente
            nombre = input("Ingrese el nombre del paciente: ")
            apellido = input("Ingrese los apellidos del paciente: ")
            tipo_documento = input(
                "Ingrese el tipo de documento del paciente (CC/TI/DIG): ")
            documento_identidad = input(
                "Ingrese el documento de identidad del paciente: ")
            while True:
                fecha_nacimiento_str = input(
                    "Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
                try:
                    fecha_nacimiento = date.fromisoformat(fecha_nacimiento_str)
                    break
                except ValueError: 
                    print(
                        "Formato de fecha incorrecto. Por favor, ingrese la fecha en formato YYYY-MM-DD.")
            paciente = Paciente(nombre=nombre, apellido=apellido, tipo_documento=tipo_documento,
                                documento_identidad=documento_identidad, fecha_nacimiento=fecha_nacimiento)
            gestion_pacientes.agregar_paciente(paciente)
        elif opcion == "3":
            # Actualizar paciente
            documento_identidad = input(
                "Ingrese el documento de identidad del paciente que desea actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre del paciente: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del paciente: ")
            if gestion_pacientes.actualizar_paciente(documento_identidad, nuevo_nombre, nuevo_apellido):
                print("Paciente actualizado correctamente.")
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")
        elif opcion == "4":
            # Borrar paciente
            documento_identidad = input(
                "Ingrese el documento de identidad del paciente que desea borrar: ")
            if gestion_pacientes.borrar_paciente(documento_identidad):
                print("Paciente borrado correctamente.")
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")
        elif opcion == "5":
            # Asignar cita
            documento_identidad = input(
                "Ingrese el documento de identidad del paciente: ")
            paciente = gestion_pacientes.buscar_paciente(documento_identidad)
            if paciente:
                if paciente.cita:
                    print(
                        f"El paciente {paciente.nombre} {paciente.apellido} ya tiene una cita asignada.")
                else:
                    while True:
                        gestion_medico.mostrar_medicos_disponibles()
                        rm_medico = input(
                            "Ingrese el número de registro médico (RM) del médico: ")
                        medico = gestion_medico.buscar_medico_por_rm(rm_medico)
                        if medico:
                            break
                        else:
                            print(
                                "No se encontró ningún médico con ese número de registro médico. Intente nuevamente.")

                    # Si se encuentra un médico válido, solicitar la fecha_programacion, hora_asignacion y duracion al usuario
                    fecha_programacion = input(
                        "Ingrese la fecha de la cita (YYYY-MM-DD): ")
                    fecha_programacion = datetime.strptime(
                        fecha_programacion, "%Y-%m-%d")  # convertir a objeto datetime
                    hora_asignacion = input(
                        "Ingrese la hora de la cita (HH:MM): ")
                    # Convertir la hora de asignación a un objeto time
                    hora_asignacion = datetime.strptime(
                        hora_asignacion, "%H:%M").time()
                    duracion = int(
                        input("Ingrese la duración de la cita en minutos: "))
                    gestion_citas.asignar_cita(
                        paciente, rm_medico, fecha_programacion, hora_asignacion, duracion)
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")

        elif opcion == "6":
            # Cancelar cita
            documento_identidad = input(
                "Ingrese el documento de identidad del paciente: ")
            paciente = gestion_pacientes.buscar_paciente(documento_identidad)
            if paciente:
                gestion_citas.cancelar_cita(paciente)
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")
        elif opcion == "7":
            # Mostrar citas
            gestion_citas.mostrar_citas()
        elif opcion == "8":
            # Ver médicos disponibles
            gestion_medico.mostrar_medicos_disponibles()
        elif opcion == "9":
            # Salir
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()
