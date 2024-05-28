from datetime import datetime
import pandas as pd
from medicos.medico import Medico
from medicos.malla import Malla

class GestionDeMedicos:
    def __init__(self):
        self.medicos = []  # Lista de médicos preestablecidos
    
    def cargar_medicos_desde_excel(self, ruta_excel_medicos):
        try:
            medicos_df = pd.read_excel(ruta_excel_medicos, sheet_name='medicos')
            print("Datos de médicos leídos desde el archivo Excel:")
            #print(medicos_df)  # Imprimir el DataFrame para verificar los datos
            
            for index, row in medicos_df.iterrows():
                print(f"Fila {index}: {row}")  # Imprimir cada fila para depuración
                datos_medico = {
                    'nombre': row['nombre'],
                    'apellido': row['apellido'],
                    'especialidad': row['especialidad'],
                    'numero_rm': row['numero_rm'],
                    'consultorio': row['consultorio']
                }
                medico = Medico(datos_medico)
                self.medicos.append(medico)
            print("Médicos cargados exitosamente desde el archivo Excel.")
        except Exception as e:
            print(f"Error al cargar datos de médicos desde el archivo Excel: {e}")
        
        self.generarCitasVacias()

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_medicos_disponibles(self):
        if self.medicos:
            print("Médicos disponibles:")
            for medico in self.medicos:
                print(f"Nombre: {medico.nombre}, Especialidad: {medico.especialidad}, RM: {medico.numero_rm}, Consultorio: {medico.consultorio}")
        else:
            print("No hay médicos disponibles")
    
    def buscar_medico_por_rm(self, rm_medico):
        print(f"Buscando médico con RM: {rm_medico}")  # Añadir esta línea para depuración
        for medico in self.medicos:
            if str(medico.numero_rm) == str(rm_medico):
                return medico
        return None

    def generarCitasVacias(self):
        for medico in self.medicos:
            malla = Malla()
            medico.citas = malla.generarMalla()
