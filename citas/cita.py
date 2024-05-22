from datetime import datetime

class Cita:
    def __init__(self, paciente, medico, fecha_solicitud, fecha_programacion, hora_asignacion, consultorio):
        self.paciente = paciente
        self.medico = medico
        self.fecha_solicitud = fecha_solicitud
        self.fecha_programacion = fecha_programacion
        self.hora_asignacion = hora_asignacion
        self.consultorio = consultorio
        self.estado = 'no disponible'

    def asignar_medico(self, medico):
        self.medico = medico
    
    def __str__(self):
        return f"Cita: {self.paciente.nombre} {self.paciente.apellido} con Dr. {self.medico.nombre} en consultorio {self.consultorio} el {self.fecha_programacion} a las {self.hora_asignacion}. Estado: {self.estado}"
    
    def cancelar(self):
        self.estado = "disponible"
    
    def __repr__(self):
        return f"Cita({self.fecha_prog.strftime('%Y-%m-%d')}, {self.hora}, {self.num_consultorio}, {self.medico.nombre}, {self.paciente.nombres}, {self.estado})"
