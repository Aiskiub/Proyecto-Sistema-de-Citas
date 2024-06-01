from datetime import datetime

class Cita:
    def __init__(self, paciente, medico, fecha_programacion, hora_asignacion):
        self.paciente = paciente
        self.medico = medico
        self.fecha_programacion = fecha_programacion
        self.hora_asignacion = hora_asignacion
        self.consultorio = medico.consultorio
        self.fechaSolicitud = datetime.now()
    
    def __str__(self):
        return f"Cita: {self.paciente.nombre} {self.paciente.apellido} con Dr. {self.medico.nombre} {self.medico.apellido} en consultorio {self.medico.consultorio} el {self.fecha_programacion} a las {self.hora_asignacion}."
    