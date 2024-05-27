from datetime import timedelta  # No se porque sirve con , datetime
from datetime import datetime
from citas.cita import Cita

class GestionDeCitas:
    def __init__(self):
        self.medicos = []  # Lista de médicos preestablecidos
        self.citas = []  # Lista para almacenar las citas médicas

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def asignar_cita(self, paciente, medico_nombre, hora_inicio, duracion):
        try:
            hora_inicio = datetime.strptime(hora_inicio, '%Y-%m-%d %H:%M')
            duracion = timedelta(minutes=duracion)
        except ValueError as e:
            print(f"Error al parsear la fecha/hora: {e}")
            return False
        
        nueva_cita = Cita(paciente, None, datetime.now().strftime('%Y-%m-%d'), hora_inicio.strftime('%Y-%m-%d'), hora_inicio.strftime('%H:%M'))
        
        for medico in self.medicos:
            if medico.nombre == medico_nombre:
                if medico.verificar_disponibilidad(hora_inicio, nueva_cita.hora_asignacion, duracion):
                    nueva_cita.asignar_medico(medico)
                    medico.agregar_cita(nueva_cita)
                    paciente.cita = nueva_cita
                    self.citas.append(nueva_cita)
                    print(f"Cita asignada: {nueva_cita}")
                    return True
                else:
                    print(f"El médico {medico.nombre} no está disponible en ese horario.")
                    return False
        
        print(f"No se encontró al médico {medico_nombre}.")
        return False

    def cancelar_cita(self, paciente):
        if paciente.cita:
            cita = paciente.cita
            cita.cancelar()
            cita.medico.citas.remove(cita)
            self.citas.remove(cita)
            paciente.cita = None
            print(f"Cita cancelada para {paciente.nombre} {paciente.apellido}")
            return True
        print(f"No hay cita para cancelar para {paciente.nombre} {paciente.apellido}")
        return False

    def mostrar_citas(self):
        for cita in self.citas:
            print(cita)
