from datetime import timedelta, datetime
from citas.cita import Cita
from medicos.medico import Medico
import pandas as pd

class GestionDeCitas:
    def __init__(self):
        self.medicos = []  # Lista de médicos preestablecidos
        self.citas = []  # Lista para almacenar las citas médicas

    def cargar_medicos_desde_excel(self, excel_file):
        try:
            medicos_df = pd.read_excel(excel_file, sheet_name='medicos')
            for index, row in medicos_df.iterrows():
                medico = Medico(row)
                self.medicos.append(medico)
            print("Médicos cargados exitosamente desde el archivo Excel.")
        except Exception as e:
            print(f"Error al cargar datos de médicos desde el archivo Excel: {e}")

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def asignar_cita(self, paciente, medico_nombre, hora_inicio, duracion):
        try:
            hora_inicio = datetime.strptime(hora_inicio, '%Y-%m-%d %H:%M')
            duracion = timedelta(minutes=duracion)
        except ValueError as e:
            print(f"Error al parsear la fecha/hora: {e}")
            return False
        
        # Obtener el médico correspondiente por su nombre
        medico = next((med for med in self.medicos if med.nombre == medico_nombre), None)
        
        if medico:
            # Obtener el consultorio del médico
            consultorio = medico.consultorio
            
            # Crear la nueva cita con el consultorio obtenido
            nueva_cita = Cita(paciente, None, datetime.now().strftime('%Y-%m-%d'), hora_inicio.strftime('%Y-%m-%d'), hora_inicio.strftime('%H:%M'), consultorio)

            if medico.verificar_disponibilidad(hora_inicio, nueva_cita.hora_asignacion, duracion):
                # Establecer el médico en la cita
                nueva_cita.medico = medico
                medico.agregar_cita(nueva_cita)
                paciente.cita = nueva_cita
                self.citas.append(nueva_cita)
                print(f"Cita asignada: {nueva_cita}")
                return True
            else:
                print(f"El médico {medico.nombre} no está disponible en ese horario.")
                return False
        else:
            print(f"No se encontró al médico {medico_nombre}.")
            return False


    def cancelar_cita(self, paciente):
        if paciente.cita:
            cita = paciente.cita
            cita.estado = 'cancelada'
            cita.medico.citas.remove(cita)
            self.citas.remove(cita)
            paciente.cita = None
            print(f"Cita cancelada para {paciente.nombre} {paciente.apellido}")
            return True
        print(f"No hay cita para cancelar para {paciente.nombre} {paciente.apellido}")
        return False

    def mostrar_citas(self):
        for cita in self.citas:
            print(cita)
        else:
            print("No hay citas programadas aún")
