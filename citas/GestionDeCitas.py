from datetime import timedelta, datetime, time
from citas.cita import Cita
from medicos.medico import Medico
from medicos.GestionDeMedicos import GestionDeMedicos
import pandas as pd

class GestionDeCitas:
    def __init__(self, gestion_medicos):
        self.citas = []  # Lista para almacenar las citas médicas
        self.gestion_medicos = gestion_medicos  # Guardar la instancia de GestionDeMedicos

    def asignar_cita(self, paciente, medico_rm, fecha_programacion, hora_asignacion, duracion):
        # Buscar al médico por su número de registro médico (RM)
        print(f"RM del médico a buscar: {medico_rm}")  # Añadir esta línea para depuración
        medico = self.gestion_medicos.buscar_medico_por_rm(medico_rm)
        if medico:
            print(f"Médico encontrado: {medico}")  # Añadir esta línea para depuración
            # Convertir la fecha de programación y la hora de asignación a objetos datetime completos
            fecha_hora_programacion = datetime.combine(fecha_programacion, hora_asignacion)
            
            # Verificar la disponibilidad del médico para la fecha y hora especificadas
            if medico.verificar_disponibilidad(fecha_hora_programacion.date(), fecha_hora_programacion.time(), duracion):
                # Crear la cita con la información proporcionada
                nueva_cita = Cita(paciente, medico, fecha_hora_programacion, hora_asignacion, duracion, medico.consultorio)
                paciente.cita = nueva_cita
                self.citas.append(nueva_cita)
                # Agregar la cita a la malla de citas del médico
                medico.agregar_cita(nueva_cita)
                print(f"Cita asignada: {nueva_cita}")
                return True
            else:
                print("El médico no está disponible en ese horario.")
                return False  # Agregado para salir del método en caso de no estar disponible
        else:
            print("No se encontró al médico con el número de registro médico especificado.")
            return False  # Agregado para salir del método en caso de no encontrar al médico


    def cancelar_cita(self, paciente):
        if paciente.cita:
            cita = paciente.cita
            cita.estado = 'cancelada'
            cita.medico.cancelar_cita(cita)
            self.citas.remove(cita)
            paciente.cita = None
            print(f"Cita cancelada para {paciente.nombre} {paciente.apellido}")
            return True
        print(f"No hay cita para cancelar para {paciente.nombre} {paciente.apellido}")


    def mostrar_citas(self):
        if self.citas:
            for cita in self.citas:
                print(cita)
        else:
            print("No hay citas programadas aún")
