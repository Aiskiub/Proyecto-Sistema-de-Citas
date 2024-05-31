from datetime import datetime

class Cita:
    def __init__(self, paciente, medico, fecha_programacion, hora_asignacion, duracion, consultorio):
        self.paciente = paciente
        self.medico = medico
        self.fecha_programacion = fecha_programacion
        self.hora_asignacion = hora_asignacion
        self.duracion = duracion
        self.consultorio = consultorio
        self.estado = 'Asignado'
        # Combinar fecha_programacion y hora_asignacion en un objeto datetime
        self.fecha_hora_programacion = datetime(
            fecha_programacion.year,
            fecha_programacion.month,
            fecha_programacion.day,
            hora_asignacion.hour,
            hora_asignacion.minute,
            hora_asignacion.second
        )
    
    def __str__(self):
        return f"Cita: {self.paciente.nombre} {self.paciente.apellido} con Dr. {self.medico.nombre} {self.medico.apellido} en consultorio {self.medico.consultorio} el {self.fecha_programacion} a las {self.hora_asignacion}. Estado: {self.estado}"
