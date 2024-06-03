from datetime import datetime
from citas.cita import Cita
from medicos.medico import Medico
from medicos.GestionDeMedicos import GestionDeMedicos
from utils.RadixSort import radix_sort_citas, counting_sort_citas

class GestionDeCitas:
    def __init__(self, gestion_medicos):
        self.citas = []  # Lista para almacenar la cola de citas médicas
        self.gestion_medicos = gestion_medicos  # Guardar la instancia de GestionDeMedicos

    def asignar_cita(self, paciente, medico, fecha_str, hora):
        # Convertir fecha y hora a objeto datetime
        fecha_programacion = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        duracion = 30  # Duración de la cita en minutos
        
        # Verificar disponibilidad antes de asignar la cita
        if medico.verificar_disponibilidad(fecha_programacion, hora, duracion):
            # Crear la cita con la información proporcionada
            cita = Cita(paciente, medico, fecha_programacion, hora, duracion)
            paciente.cita = cita
            self.citas.append(cita)
            # Agregar la cita a la malla de citas del médico
            medico.agregar_cita(cita)
            medico.eliminar_horario_disponible(fecha_programacion, hora)  # Eliminar horario disponible
            print(f"Cita asignada: {cita}")
            return True
        else:
            print(f"El horario {hora} el {fecha_str} no está disponible para el Dr. {medico.nombre} {medico.apellido}.")
            return False

    def cancelar_cita(self, paciente):
        # Elimina la cita de la malla del médico, de la cola de citas y del
        # atributo del paciente
        if paciente.cita != -1:
            cita = paciente.cita
            cita.medico.cancelar_cita(cita)
            self.citas.remove(cita)
            cita.medico.agregar_horario_disponible(cita.fecha_programacion, cita.hora_asignacion)
            paciente.cita = None
            print(f"Cita cancelada para {paciente.nombre} {paciente.apellido}")
            return True
        print(f"No hay cita para cancelar para {paciente.nombre} {paciente.apellido}")

    def mostrar_citas(self):
        if self.citas:
            self.ordenar_citas_por_fecha()
            for cita in self.citas:
                print(cita)
        else:
            print("No hay citas programadas aún")

    def ordenar_citas_por_fecha(self):
        radix_sort_citas(self.citas)
