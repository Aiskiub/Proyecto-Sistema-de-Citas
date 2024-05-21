class Medico:
    def __init__(self, nombre, apellido, registro_medico):
        self.nombre = nombre
        self.apellido = apellido
        self.registro_medico = registro_medico
        self.malla_citas = []

    def agregarCita(self, cita):
        self.malla_citas.append(cita)

    def cancelarCita(self, cita):
        if cita in self.malla_citas:
            self.malla_citas.remove(cita)
            return True
        return False

    def estaDisponible(self, fecha, hora):
        for cita in self.malla_citas:
            if cita.fecha == fecha and cita.hora == hora:
                return False
        return True






