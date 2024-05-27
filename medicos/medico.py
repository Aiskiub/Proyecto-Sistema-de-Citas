import pandas as pd
from datetime import datetime, timedelta
import os

class Medico:
    def __init__(self, datos_medico):
        self.nombre = datos_medico['nombre']
        self.apellido = datos_medico['apellido']
        self.especialidad = datos_medico['especialidad']
        self.numero_rm = datos_medico['numero_rm']
        self.consultorio = datos_medico['consultorio']
        self.citas = []  # Lista para las citas del médico
    
    def verificar_disponibilidad(self, fecha_programacion, hora_asignacion, duracion):
        for cita in self.citas:
            cita_inicio = datetime.combine(cita.fecha_programacion, cita.hora_asignacion)
            cita_fin = cita_inicio + timedelta(minutes=cita.duracion)
            nueva_cita_inicio = datetime.combine(fecha_programacion, hora_asignacion)
            nueva_cita_fin = nueva_cita_inicio + timedelta(minutes=duracion)
            
            if not (nueva_cita_fin <= cita_inicio or nueva_cita_inicio >= cita_fin):
                return False
        return True
    
    def ordenar_citas(self):
        self.citas.sort(key=lambda cita: (cita.fecha_programacion, cita.hora_asignacion))
    
    def agregar_cita(self, cita):
        self.citas.append(cita)
        self.ordenar_citas()
    
    def cancelar_cita(self, cita):
        self.citas.remove(cita)
        self.ordenar_citas()

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} ({self.especialidad}), RM: {self.numero_rm}"
