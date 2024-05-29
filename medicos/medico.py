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
        fechaCita= cita.fecha_programacion
        horaCita = cita.hora_asignacion
        
        #Modificar disponibilidad en malla a 'false'
        malla = self.citas
        mallaFecha = malla[fechaCita]
        mallaFecha[horaCita] = 'false'
        

    def cancelar_cita(self, cita):
        #Cambia disponibilidad de cita cancelada en la malla del médico
        fecha = cita.fecha_programacion
        hora = cita.hora_asignacion
        mallaFecha = self.citas[fecha[hora]] = 'true'

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} ({self.especialidad}), RM: {self.numero_rm}"
    
    def generarCitas(self):
        malla = Malla()
        self.citas = malla.generarMalla()
        print (self.citas)
    
    

    
