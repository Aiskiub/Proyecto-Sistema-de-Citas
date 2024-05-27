import pandas as pd
from datetime import datetime, timedelta
import os
from medicos.malla import Malla

class Medico:
    def __init__(self, datos_medico):
        self.nombre = datos_medico['nombre']
        self.apellido = datos_medico['apellido']
        self.especialidad = datos_medico['especialidad']
        self.numero_rm = datos_medico['numero_rm']
        self.consultorio = datos_medico['consultorio']
        self.citas = {}  #Diccionario para almacenar la malla de citas del médico
    
    def verificar_disponibilidad(self, fecha_programacion, hora_asignacion, duracion):
        for citas_en_fecha in self.citas.values():
            for cita in citas_en_fecha:
                cita_inicio = datetime.combine(cita.fecha_programacion, cita.hora_asignacion)
                cita_fin = cita_inicio + timedelta(minutes=cita.duracion)
                nueva_cita_inicio = datetime.combine(fecha_programacion, hora_asignacion)
                nueva_cita_fin = nueva_cita_inicio + timedelta(minutes=duracion)
                
                if not (nueva_cita_fin <= cita_inicio or nueva_cita_inicio >= cita_fin):
                    return False
        return True
    
    def agregar_cita(self, cita):
        # Obtener la fecha y hora de programación de la cita
        fecha_hora_programacion = cita.fecha_hora_programacion
        
        # Verificar si ya existe una lista de citas para esa fecha
        if fecha_hora_programacion.date() not in self.citas:
            # Si no existe, crear una nueva lista de citas para esa fecha
            self.citas[fecha_hora_programacion.date()] = []
        
        # Agregar la cita a la lista de citas para esa fecha
        self.citas[fecha_hora_programacion.date()].append(cita)

    def cancelar_cita(self, cita):
        # Obtener la fecha de programación de la cita
        fecha_programacion = cita.fecha_programacion.date()
        
        # Verificar si existe una lista de citas para esa fecha
        if fecha_programacion in self.citas:
            # Si existe, eliminar la cita de la lista de citas para esa fecha
            self.citas[fecha_programacion].remove(cita)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} ({self.especialidad}), RM: {self.numero_rm}"
    
    def generarCitas(self):
        malla = Malla()
        self.citas = malla.generarMalla()
        print (self.citas)
    
