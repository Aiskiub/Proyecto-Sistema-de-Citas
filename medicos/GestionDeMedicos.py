from datetime import datetime
import pandas as pd
from medicos.medico import Medico
from medicos.malla import Malla
from utils.logger import Logger as log

class GestionDeMedicos:
    def __init__(self):
        self.medicos = []  # Lista de médicos preestablecidos

    def cargar_medicos_desde_excel(self, ruta_excel_medicos):
        try:
            # Leer el archivo Excel y cargar los datos en un DataFrame de la libreria pandas
            medicos_df = pd.read_excel(ruta_excel_medicos, sheet_name='medicos')
            log.success("Datos de médicos leídos desde el archivo Excel:")
            # Imprimir el DataFrame para verificar los datos (puede ser comentado o eliminado en pruebas)
            #print(medicos_df)
            
            # Iterar sobre cada fila del DataFrame
            for index, row in medicos_df.iterrows():
                # Imprimir cada fila para depuración (puede ser comentado o eliminado en producción)
                #print(f"Fila {index}: {row}")
                # Crear un diccionario con los datos del médico
                datos_medico = {
                    'nombre': row['nombre'],
                    'apellido': row['apellido'],
                    'especialidad': row['especialidad'],
                    'numero_rm': row['numero_rm'],
                    'consultorio': row['consultorio']
                }
                # Crear una instancia de Medico con los datos obtenidos
                medico = Medico(datos_medico)
                # Agregar la instancia de Medico a la lista de médicos
                self.medicos.append(medico)
            log.success("Médicos cargados exitosamente desde el archivo Excel.")
        except Exception as e:
            # Manejar cualquier error que ocurra durante la lectura del archivo Excel
            log.error(f"Error al cargar datos de médicos desde el archivo Excel: {e}")
        
        # Generar citas vacías para cada médico después de cargar los datos, para añadirlos a la malla
        self.generarCitasVacias()

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_medicos_disponibles(self):
        # Mostrar la lista de médicos disponibles
        if self.medicos:
            print("Médicos disponibles:")
            for medico in self.medicos:
                print(f"Nombre: {medico.nombre}, Especialidad: {medico.especialidad}, RM: {medico.numero_rm}, Consultorio: {medico.consultorio}")
        else:
            # Mostrar un mensaje si no hay médicos disponibles
            print("No hay médicos disponibles")
    
    def buscar_medico_por_rm(self, rm_medico):
        # Buscar un médico por su número de registro médico (RM)
        print(f"Buscando médico con RM: {rm_medico}")  # Añadir esta línea para depuración
        for medico in self.medicos:
            if str(medico.numero_rm) == str(rm_medico):
                # Devolver la instancia de Medico si se encuentra una coincidencia
                return medico
        # Devolver None si no se encuentra el médico
        return None

    def generarCitasVacias(self):
        # Generar citas vacías para cada médico en la lista de médicos
        for medico in self.medicos:
            malla = Malla()  # Crear una instancia de Malla
            medico.citas = malla.generarMalla()  # Asignar la malla generada al médico
