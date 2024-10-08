import pandas as pd
from medicos.medico import Medico
from medicos.buscarCitasDisponibles import buscarCitasDisponibles
from pacientes.paciente import Paciente
from pacientes.GestionDePacientes import GestionDePacientes
from pacientes.actualizarPacientes import actualizarDatos
from pacientes.mostrarPacientes import mostrarPacientes
from citas.GestionDeCitas import GestionDeCitas
from citas.cita import Cita
from datetime import date, datetime, time
from medicos.GestionDeMedicos import GestionDeMedicos
import os
from utils.logger import Logger as log
def main():

    # Aquí se crean instancias de Gestión de Pacientes y Gestión de Citas
    gestion_pacientes = GestionDePacientes()
    gestion_medico = GestionDeMedicos()

    # Ruta relativa al archivo Excel (NO CAMBIAR)
    ruta_excel_medicos = './excel/archivo.xlsx'
    ruta_excel_pacientes = './excel/pacientes.xlsx'

    # Verificar si los archivos existen
    if not os.path.exists(ruta_excel_medicos):
        log.error(f"El archivo de médicos no existe: {ruta_excel_medicos}")
        return

    if not os.path.exists(ruta_excel_pacientes):
        log.error(f"El archivo de pacientes no existe: {ruta_excel_pacientes}")
        return

    # Cargar datos de médicos desde el archivo Excel
    gestion_medico.cargar_medicos_desde_excel(ruta_excel_medicos)

    # Crear instancia de GestionDeCitas y pasarle la instancia de GestionDeMedicos
    gestion_citas = GestionDeCitas(gestion_medico)

    # Cargar datos de pacientes desde el archivo Excel
    gestion_pacientes.cargar_pacientes_desde_excel(ruta_excel_pacientes)

    while True:
        print("\nMenú de opciones:")
        print("1. Leer pacientes")
        print("2. Agregar paciente")
        print("3. Actualizar paciente")
        print("4. Borrar paciente")
        print("5. Asignar cita")
        print("6. Cancelar cita")
        print("7. Mostrar citas")
        print("8. Ver médicos disponibles")
        print("9. Salir\n")
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            # Leer pacientes
            pilaPacientes = gestion_pacientes.leer_pacientes()
            print("Pacientes en la pila:")
            mostrarPacientes(pilaPacientes)

        elif opcion == "2":
            # Agregar paciente
            nombre = input("Ingrese el nombre del paciente: ")
            apellido = input("Ingrese los apellidos del paciente: ")
            tipo_documento = ""
            while tipo_documento not in ["CC", "TI", "PA", "DIG"]:
                tipo_documento = input("Ingrese el tipo de documento del paciente (CC/TI/PA/DIG): ")
                if tipo_documento not in ["CC", "TI", "PA", "DIG"]:
                    log.error("Tipo de documento incorrecto. Por favor, ingrese uno de los siguientes: CC, TI, PA, DIG.")
            
            documento_identidad = ""
            while not documento_identidad.isdigit():
                documento_identidad = input("Ingrese el documento de identidad del paciente (solo números): ")
                if not documento_identidad.isdigit():
                    log.error("Documento de identidad incorrecto. Por favor, ingrese solo números.")
            
            while True:
                fecha_nacimiento_str = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
                try:
                    fecha_nacimiento = date.fromisoformat(fecha_nacimiento_str)
                    break
                except ValueError:
                    log.error("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato YYYY-MM-DD.")
            
            paciente = Paciente(nombre=nombre, apellido=apellido, tipo_documento=tipo_documento,
                                documento_identidad=documento_identidad, fecha_nacimiento=fecha_nacimiento)
            gestion_pacientes.agregar_paciente(paciente)

        elif opcion == "3":
            # Actualizar paciente
            documento_identidad = input("Ingrese el documento de identidad del paciente que desea actualizar: ")
            paciente = gestion_pacientes.buscar_paciente(documento_identidad)
            if paciente != -1: 
                actualizarDatos(gestion_pacientes, paciente)
            else:
                pacienteNotFound()
        elif opcion == "4":
            # Borrar paciente
            documento_identidad = ""
            while not documento_identidad.isdigit():
                documento_identidad = input("Ingrese el documento de identidad del paciente que desea borrar (solo números): ")
                if not documento_identidad.isdigit():
                    log.error("Documento de identidad incorrecto. Por favor, ingrese solo números.")
            
            if gestion_pacientes.borrar_paciente(int(documento_identidad)):
                log.success("Paciente borrado correctamente.")
            else:
                pacienteNotFound()
        elif opcion == "5":
            # Asignar cita
            documento_identidad = ""
            while not documento_identidad.isdigit():
                documento_identidad = input("Ingrese el documento de identidad del paciente (solo números): ")
                if not documento_identidad.isdigit():
                    log.error("Documento de identidad incorrecto. Por favor, ingrese solo números.")
            paciente = gestion_pacientes.buscar_paciente(documento_identidad)
            if paciente != -1: #La vieja confiable
                if paciente.cita:
                    print(f"El paciente {paciente.nombre} {paciente.apellido} ya tiene una cita asignada.")
                else:
                    while True:
                        gestion_medico.mostrar_medicos_disponibles()
                        rm_medico = input("Ingrese el número de registro médico (RM) del médico: ")
                        medico = gestion_medico.buscar_medico_por_rm(rm_medico)
                        if medico:
                            fecha_str = input("Ingrese una fecha para agendar su cita (dd/mm/yyyy): ")
                            try:
                                fecha_programacion = datetime.strptime(fecha_str, "%d/%m/%Y").date()
                                if buscarCitasDisponibles(medico, fecha_str):
                                    hora = input("Seleccione un horario disponible (HH:MM): ")
                                    if gestion_citas.asignar_cita(paciente, medico, fecha_str, hora):
                                        break
                                    else:
                                        log.info("Intente nuevamente con otra fecha u horario.")
                            except ValueError:
                                log.error("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato dd/mm/yyyy.")
                        else:
                            log.error("No se encontró ningún médico con ese número de registro médico. Intente nuevamente.")
            else:
                pacienteNotFound()
        elif opcion == "6":
            # Cancelar cita
            documento_identidad = input("Ingrese el documento de identidad del paciente: ")
            paciente = gestion_pacientes.buscar_paciente(documento_identidad)
            if paciente != -1:
                gestion_citas.cancelar_cita(paciente)
            else:
                pacienteNotFound()
        elif opcion == "7":
            # Mostrar citas
            gestion_citas.mostrar_citas()
        elif opcion == "8":
            # Ver médicos disponibles
            gestion_medico.mostrar_medicos_disponibles()
        elif opcion == "9":
            # Salir
            log.info("Saliendo del programa...")
            break
    
        else:
            log.error("Opción no válida. Por favor, ingrese un número válido.")

def pacienteNotFound():
    log.error("No se encontró ningún paciente con ese documento de identidad.")

if __name__ == "__main__":
    main()
