from datetime import datetime, timedelta

class Medico:
    def __init__(self, datos_medico):
        self.nombre = datos_medico['nombre'] 
        self.apellido = datos_medico['apellido'] 
        self.especialidad = datos_medico['especialidad'] 
        self.numero_rm = datos_medico['numero_rm'] 
        self.consultorio = datos_medico['consultorio']  
        self.citas = {}  # Diccionario para almacenar la malla de citas del médico
    
    def verificar_disponibilidad(self, fecha_programacion, hora_asignacion, duracion):
        # Verificar si un horario está disponible
        fecha_str = fecha_programacion.strftime("%d/%m/%Y")
        if fecha_str not in self.citas:
            self.citas[fecha_str] = self.generar_horarios_disponibles()
        if self.citas[fecha_str].get(hora_asignacion) == 'false':
            return False  # Retorna False si el horario está ocupado
        return True  # Retorna True si el horario está disponible
    
    def agregar_cita(self, cita):
        # Agregar una cita a la malla del médico
        fecha_str = cita.fecha_programacion.strftime("%d/%m/%Y")
        if fecha_str not in self.citas:
            self.citas[fecha_str] = self.generar_horarios_disponibles()
        self.citas[fecha_str][cita.hora_asignacion] = 'false'  # Marcar la franja horaria como ocupada
        print(f"Cita agregada: {cita}")

    def eliminar_horario_disponible(self, fecha_programacion, hora_asignacion):
        # Marcar un horario como ocupado
        fecha_str = fecha_programacion.strftime("%d/%m/%Y")
        if fecha_str in self.citas:
            self.citas[fecha_str][hora_asignacion] = 'false'
    
    def agregar_horario_disponible(self, fecha_programacion, hora_asignacion):
        # Marcar un horario como disponible
        fecha_str = fecha_programacion.strftime("%d/%m/%Y")
        if fecha_str in self.citas:
            self.citas[fecha_str][hora_asignacion] = 'true'
        else:
            self.citas[fecha_str] = self.generar_horarios_disponibles()
            self.citas[fecha_str][hora_asignacion] = 'true'
    
    def cancelar_cita(self, cita):
        # Cancelar una cita y liberar el horario
        fecha_str = cita.fecha_programacion.strftime("%d/%m/%Y")
        if fecha_str in self.citas and cita.hora_asignacion in self.citas[fecha_str]:
            self.citas[fecha_str][cita.hora_asignacion] = 'true'
            print(f"Cita cancelada: {cita}")

    def generar_horarios_disponibles(self):
        # Generar horarios disponibles para un día de trabajo
        horarios = {}
        hora_inicio = datetime.strptime('08:00', '%H:%M')  # Hora de inicio de la jornada
        hora_fin = datetime.strptime('16:00', '%H:%M')  # Hora de fin de la jornada
        duracion_cita = timedelta(minutes=30)  # Duración de cada cita
        while hora_inicio <= hora_fin:
            horarios[hora_inicio.strftime('%H:%M')] = 'true'  # Marcar la franja horaria como disponible
            hora_inicio += duracion_cita  # Incrementar la hora según la duración de la cita
        return horarios

    def __str__(self):
        # Representación en string del médico
        return f"Dr. {self.nombre} {self.apellido} ({self.especialidad}), RM: {self.numero_rm}"