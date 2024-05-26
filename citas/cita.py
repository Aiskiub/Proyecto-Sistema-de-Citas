import utils.algoritmos as utils
from collections import deque

class MallaCitas:
    def __init__(self):
        self.citas = deque()

    def agregarCita(self, cita):
        self.citas.append(cita)

    def cancelarCita(self, cita):
        if cita in self.citas:
            self.citas.remove(cita)
            return True
        return False

    def buscarCita(self, fecha, hora):
        for cita in self.citas:
            if cita.fecha_programacion == fecha and cita.hora_asignacion == hora:
                return cita
        return None
    
    

