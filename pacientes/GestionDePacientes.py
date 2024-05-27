from utils.stack_pacientes import Stack
import pandas as pd
from pacientes.paciente import Paciente
from datetime import datetime

class GestionDePacientes:
    def __init__(self):
        self.pila_pacientes = Stack()  # Cambiamos la lista por una pila
    
    def cargar_pacientes_desde_excel(self, ruta_excel_pacientes):
        try:
            pacientes_df = pd.read_excel(ruta_excel_pacientes, sheet_name='pacientes')
            print("Datos de pacientes leídos desde el archivo Excel:")
            #print(pacientes_df)  # Imprimir el DataFrame para verificar los datos
            
            for index, row in pacientes_df.iterrows():
                nombre = row['nombre']
                apellido = row['apellido']
                tipo_documento = row['tipo_documento']
                documento_identidad = str(row['documento_identidad'])  # Convertir a cadena
                fecha_nacimiento = row['fecha_nacimiento'].date()  # Convertir a objeto datetime.date
                
                # Crear objeto Paciente con los datos obtenidos
                paciente = Paciente(nombre, apellido, tipo_documento, documento_identidad, fecha_nacimiento)
                self.pila_pacientes.push(paciente)

            print("Pacientes cargados exitosamente desde el archivo Excel.")
        except Exception as e:
            print(f"Error al cargar datos de pacientes desde el archivo Excel: {e}")

    def agregar_paciente(self, paciente):
        self.pila_pacientes.push(paciente)
    
    def leer_pacientes(self):
        pacientes = []
        current_node = self.pila_pacientes.top
        while current_node is not None:
            paciente = current_node.valor
            pacientes.append(paciente)
            current_node = current_node.next
        
        if not pacientes:
            print("No hay pacientes en la pila.")
        return pacientes

    
    def buscar_paciente(self, documento_identidad):
        current_node = self.pila_pacientes.top
        while current_node is not None:
            if current_node.valor.documento_identidad == documento_identidad:
                return current_node.valor
            current_node = current_node.next
        return None
    
    def borrar_paciente(self, documento_identidad):
        current_node = self.pila_pacientes.top
        prev_node = None
        while current_node is not None:
            if current_node.valor.documento_identidad == documento_identidad:
                if prev_node is None:
                    self.pila_pacientes.pop()  # Eliminar el primer elemento de la pila
                else:
                    prev_node.next = current_node.next  # Saltar el nodo actual
                return True
            prev_node = current_node
            current_node = current_node.next
        return False
    
    def actualizar_paciente(self, documento_identidad, nuevo_nombre, nuevo_apellido):
        current_node = self.pila_pacientes.top
        while current_node is not None:
            if current_node.valor.documento_identidad == documento_identidad:
                current_node.valor.nombre = nuevo_nombre
                current_node.valor.apellido = nuevo_apellido
                return True
            current_node = current_node.next
        return False
