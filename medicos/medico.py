from utils.busquedabinaria import busquedaBinaria
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
        fecha_str = fecha_programacion.strftime("%Y-%m-%d")
        citas_en_fecha = self.citas.get(fecha_str, [])
        nueva_cita_inicio = datetime.combine(fecha_programacion, datetime.strptime(hora_asignacion, "%H:%M").time())
        nueva_cita_fin = nueva_cita_inicio + timedelta(minutes=duracion)

        for cita in citas_en_fecha:
            cita_inicio = datetime.combine(cita.fecha_programacion, datetime.strptime(cita.hora_asignacion, "%H:%M").time())
            cita_fin = cita_inicio + timedelta(minutes=cita.duracion)
            if not (nueva_cita_fin <= cita_inicio or nueva_cita_inicio >= cita_fin):
                return False
        return True
    
    def agregar_cita(self, cita):
        fecha_str = cita.fecha_programacion.strftime("%Y-%m-%d")
        if fecha_str not in self.citas:
            self.citas[fecha_str] = []
        self.citas[fecha_str].append(cita)
        print(f"Cita agregada: {cita}")
        

    def cancelar_cita(self, cita):
        fecha_str = cita.fecha_programacion.strftime("%Y-%m-%d")
        if fecha_str in self.citas:
            self.citas[fecha_str].remove(cita)
            print(f"Cita cancelada: {cita}")

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} ({self.especialidad}), RM: {self.numero_rm}"
    
    def generarCitas(self):
        malla = Malla()
        self.citas = malla.generarMalla()
        print (self.citas)
    
    

    
