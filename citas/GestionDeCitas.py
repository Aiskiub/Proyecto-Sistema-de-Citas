from datetime import timedelta, datetime, time
from citas.cita import Cita
from medicos.medico import Medico
from medicos.GestionDeMedicos import GestionDeMedicos
import pandas as pd
from queue import Queue

class GestionDeCitas:
    def __init__(self, gestion_medicos):
        self.citas = [] # Lista para almacenar la cola de citas médicas
        self.gestion_medicos = gestion_medicos  # Guardar la instancia de GestionDeMedicos

    def asignar_cita(self, paciente, medico, fecha, hora):
       # Crear la cita con la información proporcionada
       cita = Cita(paciente, medico, fecha, hora)
       paciente.cita = cita
       self.citas.append(cita)
       # Agregar la cita a la malla de citas del médico
       medico.agregar_cita(cita)
       print(f"Cita asignada: {cita}")
       return True
  

    def cancelar_cita(self, paciente):
        #Elimina la cita de la malla del médico, de la cola de citas y del 
        #atributo del paciente
        if paciente.cita:
            cita = paciente.cita
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
