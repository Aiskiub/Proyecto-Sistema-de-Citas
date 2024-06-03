from datetime import datetime
from citas.cita import Cita
from medicos.medico import Medico
from medicos.GestionDeMedicos import GestionDeMedicos
from utils.RadixSort import radix_sort_citas

class GestionDeCitas:
    def __init__(self, gestion_medicos):
        """
        Inicializa una nueva instancia de la clase GestionDeCitas.
        """
        self.citas = []  # Lista para almacenar la cola de citas médicas
        self.gestion_medicos = gestion_medicos  # Guardar la instancia de GestionDeMedicos

    def asignar_cita(self, paciente, medico, fecha_str, hora):
        """
        Asigna una cita a un paciente con un médico en una fecha y hora específicas.
        :param paciente: Instancia del paciente.
        :param medico: Instancia del médico.
        :param fecha_str: Fecha en formato 'dd/mm/yyyy'.
        :param hora: Hora en formato 'HH:MM'.
        :return: True si la cita fue asignada, False en caso contrario.
        """
        try:
            fecha_programacion = datetime.strptime(fecha_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(f"Formato de fecha incorrecto: {fecha_str}. Use 'dd/mm/yyyy'.")

        if medico.verificar_disponibilidad(fecha_programacion, hora, 30):
            cita = Cita(paciente, medico, fecha_programacion, hora)
            paciente.cita = cita
            self.citas.append(cita)
            medico.agregar_cita(cita)
            print(f"Cita asignada: {cita}")
            return True
        else:
            print(f"El horario {hora} el {fecha_str} no está disponible para el Dr. {medico.nombre} {medico.apellido}.")
            return False

    def cancelar_cita(self, paciente):
        """
        Cancela la cita de un paciente.
        :param paciente: Instancia del paciente.
        :return: True si la cita fue cancelada, False en caso contrario.
        """
        if paciente.cita is not None:
            cita = paciente.cita
            cita.medico.cancelar_cita(cita)
            self.citas.remove(cita)
            paciente.cita = None
            print(f"Cita cancelada para {paciente.nombre} {paciente.apellido}")
            return True
        else:
            print(f"No hay cita para cancelar para {paciente.nombre} {paciente.apellido}")
            return False

    def mostrar_citas(self):
        """
        Muestra todas las citas programadas.
        """
        if self.citas:
            self.ordenar_citas_por_fecha()
            for cita in self.citas:
                print(cita)
        else:
            print("No hay citas programadas aún")

    def ordenar_citas_por_fecha(self):
        """
        Ordena las citas por fecha utilizando el algoritmo radix sort.
        """
        radix_sort_citas(self.citas)
