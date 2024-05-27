import pandas as pd
from medicos.medico import Medico
from pacientes.paciente import Paciente
from pacientes.GestionDePacientes import GestionDePacientes
from citas.GestionDeCitas import GestionDeCitas
from datetime import date
import os

def main():
    # Aquí se crean instancias de Gestión de Pacientes y Gestión de Citas
    gestion_pacientes = GestionDePacientes()
    gestion_citas = GestionDeCitas()
    
    # Ruta absoluta al archivo Excel
    excel_file = 'C:/Users/ASUS/OneDrive/Documentos/Proyecto Estructura Pruebas/archivo.xlsx'

    # Verificar si el archivo existe
    if not os.path.exists(excel_file):
        print(f"El archivo no existe: {excel_file}")
        return
    
    # Cargar datos de médicos desde el archivo Excel
    gestion_citas.cargar_medicos_desde_excel(excel_file)

    # Cargar datos de médicos desde la hoja de Excel 'medicos'
    try:
        medicos_df = pd.read_excel(excel_file, sheet_name='medicos')
    except Exception as e:
        print(f"Error al cargar datos de médicos desde el archivo Excel: {e}")
        return
        
    while True:
        print("Menú de opciones:")
        print("1. Leer pacientes")
        print("2. Agregar paciente")
        print("3. Actualizar paciente")
        print("4. Borrar paciente")
        print("5. Asignar cita")
        print("6. Cancelar cita")
        print("7. Mostrar citas")
        print("8. Salir")
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
            tipo_documento = input("Ingrese el tipo de documento del paciente (CC/TI/DIG): ")
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
            # Asignar cita
            documento_identidad = input("Ingrese el documento de identidad del paciente: ")
            paciente = gestion_pacientes.buscar_paciente(documento_identidad)
            if paciente:
                if paciente.cita:
                    print(f"El paciente {paciente.nombre} {paciente.apellido} ya tiene una cita asignada.")
                else:
                    medico_nombre = input("Ingrese el nombre del médico: ")
                    hora_inicio = input("Ingrese la fecha y hora de la cita (YYYY-MM-DD HH:MM): ")
                    duracion = int(input("Ingrese la duración de la cita en minutos: "))
                    #consultorio = input("Ingrese el número del consultorio: ")
                    gestion_citas.asignar_cita(paciente, medico_nombre, hora_inicio, duracion)
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")
        elif opcion == "6":
            # Cancelar cita
            documento_identidad = input("Ingrese el documento de identidad del paciente: ")
            paciente = gestion_pacientes.buscar_paciente(documento_identidad)
            if paciente:
                gestion_citas.cancelar_cita(paciente)
            else:
                print("No se encontró ningún paciente con ese documento de identidad.")
        elif opcion == "7":
            # Mostrar citas
            gestion_citas.mostrar_citas()
        elif opcion == "8":
            # Salir
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
