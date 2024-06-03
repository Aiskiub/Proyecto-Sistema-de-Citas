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
                ruta_excel_pacientes, sheet_name='pacientes')
            log.success("Datos de pacientes leídos desde el archivo Excel:")
            # print(pacientes_df)  # Imprimir el DataFrame para verificar los datos

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
        self.pila_pacientes.push(paciente)
        self.ordenarporDocumento()

    def leer_pacientes(self):
        pacientes = self.pila_pacientes.items
        if not pacientes:
            print("No hay pacientes en la pila.")
        return pacientes

    def buscar_paciente(self, documento_identidad):
        pila = self.pila_pacientes.items
        paciente = busquedaBinaria(pila, 
                                0, 
                                len(pila)-1, 
                                int(documento_identidad), 
                                'documento_identidad')
        return paciente

    def borrar_paciente(self, documento_identidad):
        paciente = self.buscar_paciente(documento_identidad)
        if paciente != -1:
            print(f"Nombre Paciente : {paciente.nombre}")
            self.pila_pacientes.items.remove(paciente)
            return True
        else:
            return False

    def actualizar_paciente(self, paciente, atributo, valor):
        # Convertir fecha_nacimiento a un objeto date si es necesario
        if atributo == "fecha_nacimiento" and isinstance(valor, str):
            valor = date.fromisoformat(valor)
        setattr(paciente, atributo, valor)
        if atributo == "fecha_nacimiento":
            paciente.edad = paciente.calcular_edad()
            paciente.clasificacion = paciente.clasificar()

    def ordenarporDocumento(self):
        pila = self.pila_pacientes.items
        mergeSort(pila, 0, len(pila)-1, lambda pacienteA, pacienteB:
                  int(pacienteA.documento_identidad) < int(pacienteB.documento_identidad))
        self.pila_pacientes.items = pila
        return
