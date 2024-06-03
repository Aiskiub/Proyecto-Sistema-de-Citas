from utils.stack import Stack
from utils.mergesort import mergeSort
from utils.busquedabinaria import busquedaBinaria
import pandas as pd
from pacientes.paciente import Paciente
from datetime import datetime, date
from utils.logger import Logger as log

class GestionDePacientes:
    def __init__(self):
        self.pila_pacientes = Stack()  # Cambiamos la lista por una pila

    def cargar_pacientes_desde_excel(self, ruta_excel_pacientes):
        try:
            pacientes_df = pd.read_excel(
                ruta_excel_pacientes, sheet_name='pacientes')  # Leer datos de pacientes desde un archivo Excel
            log.success("Datos de pacientes leídos desde el archivo Excel:")
            # print(pacientes_df)  # Imprimir el DataFrame para verificar los datos(puede ser comentado o eliminado en pruebas)
            for index, row in pacientes_df.iterrows():
                nombre = row['nombre']
                apellido = row['apellido']
                tipo_documento = row['tipo_documento']
                documento_identidad = str(
                    row['documento_identidad'])  # Convertir a cadena
                # Convertir a objeto datetime.date
                fecha_nacimiento = row['fecha_nacimiento'].date()

                # Crear objeto Paciente con los datos obtenidos
                paciente = Paciente(
                    nombre, apellido, tipo_documento, documento_identidad, fecha_nacimiento)
                self.agregar_paciente(paciente)

            log.success("Pacientes cargados exitosamente desde el archivo Excel.")
        except Exception as e:
            log.error(
                f"Error al cargar datos de pacientes desde el archivo Excel: {e}")

    def agregar_paciente(self, paciente):
        self.pila_pacientes.push(paciente)  # Agregar paciente a la pila
        log.success(f"Paciente agregado: {paciente.nombre} {paciente.apellido}")
        self.ordenarporDocumento()  # Ordenar la pila por documento

    def leer_pacientes(self):
        pacientes = self.pila_pacientes.items  # Obtener los pacientes de la pila
        if not pacientes:
            print("No hay pacientes en la pila.")
        return pacientes  # Devolver la lista de pacientes

    def buscar_paciente(self, documento_identidad):
        pila = self.pila_pacientes.items  # Obtener los pacientes de la pila
        paciente = busquedaBinaria(pila, 
                                0, 
                                len(pila)-1, 
                                int(documento_identidad), 
                                'documento_identidad')  # Buscar paciente por documento
        return paciente  # Devolver el paciente encontrado

    def borrar_paciente(self, documento_identidad):
        paciente = self.buscar_paciente(documento_identidad)  # Buscar el paciente
        if paciente != -1:
            print(f"Nombre Paciente : {paciente.nombre}")
            self.pila_pacientes.items.remove(paciente)  # Borrar paciente de la pila
            return True
        else:
            return False

    def actualizar_paciente(self, paciente, atributo, valor):
        # Convertir fecha_nacimiento a un objeto date si es necesario
        if atributo == "fecha_nacimiento" and isinstance(valor, str):
            valor = date.fromisoformat(valor)
        setattr(paciente, atributo, valor)  # Actualizar el atributo del paciente
        if atributo == "fecha_nacimiento":
            paciente.edad = paciente.calcular_edad()  # Recalcular la edad del paciente
            paciente.clasificacion = paciente.clasificar()  # Reclasificar al paciente

    def ordenarporDocumento(self):
        pila = self.pila_pacientes.items  # Obtener los pacientes de la pila
        mergeSort(pila, 0, len(pila)-1, lambda pacienteA, pacienteB:
                int(pacienteA.documento_identidad) < int(pacienteB.documento_identidad))  # Ordenar por documento
        self.pila_pacientes.items = pila
        return