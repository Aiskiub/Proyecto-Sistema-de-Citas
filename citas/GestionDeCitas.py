from datetime import timedelta  # No se porque sirve con , datetime
from datetime import datetime
from citas.cita import Cita


class GestionDeCitas:
    def __init__(self):
        self.medicos = []  # Lista de médicos preestablecidos
        self.citas = []  # Lista para almacenar las citas médicas

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def asignar_cita(self, paciente, medico_nombre, hora_inicio, duracion, consultorio):
        hora_inicio = datetime.strptime(hora_inicio, '%Y-%m-%d %H:%M')
        duracion = timedelta(minutes=duracion)
        nueva_cita = Cita(paciente, None, hora_inicio, duracion, consultorio)

    # Buscar al médico por nombre
        for medico in self.medicos:
            if medico.nombre == medico_nombre:
                # Verificar la disponibilidad del médico con los argumentos necesarios
                if medico.verificar_disponibilidad(nueva_cita.fecha_programacion, nueva_cita.hora_asignacion, nueva_cita.duracion):
                    # Si el médico está disponible, agregar la cita
                    medico.agregar_cita(nueva_cita)
                    paciente.cita = nueva_cita
                    self.citas.append(nueva_cita)
                    print(f"Cita asignada: {nueva_cita}")
                    return True
                else:
                    print(
                        f"El médico {medico.nombre} no está disponible en ese horario.")
                    return False
        print(f"No se encontró al médico {medico_nombre}.")
        return False

    def cancelar_cita(self, paciente):
        if paciente.cita:
            cita = paciente.cita
            cita.medico.citas.remove(cita)
            self.citas.remove(cita)
            paciente.cita = None
            print(f"Cita cancelada para {paciente.nombre} {paciente.apellido}")
            return True
        print(
            f"No hay cita para cancelar para {paciente.nombre} {paciente.apellido}")
        return False

    def mostrar_citas(self):
        for cita in self.citas:
            print(cita)
