from datetime import datetime

class Cita:
    def __init__(self, paciente, medico, fecha_solicitud, fecha_programacion, hora_asignacion, consultorio):
        self.paciente = paciente
        self.medico = medico
        self.fecha_solicitud = datetime.strptime(fecha_solicitud, "%Y-%m-%d")
        self.fecha_programacion = datetime.strptime(fecha_programacion, "%Y-%m-%d")
        self.hora_asignacion = hora_asignacion
        self.consultorio = consultorio
        self.estado = 'no disponible'

    def asignar_medico(self, medico):
        self.medico = medico
    
    def cancelar(self):
        self.estado = "disponible"
    
    def __str__(self):
        return (f"Cita: {self.paciente.nombres} {self.paciente.apellidos} con Dr. {self.medico.nombre} "
                f"en consultorio {self.consultorio} el {self.fecha_programacion.strftime('%Y-%m-%d')} "
                f"a las {self.hora_asignacion}. Estado: {self.estado}")
    
    def __repr__(self):
        return (f"Cita({self.fecha_programacion.strftime('%Y-%m-%d')}, {self.hora_asignacion}, "
                f"{self.consultorio}, {self.medico.nombre}, {self.paciente.nombres}, {self.estado})")
