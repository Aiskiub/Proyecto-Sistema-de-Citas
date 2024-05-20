import datetime

class Medico:
    def __init__(self, nombre, apellido, registro_medico):
        self.nombre = nombre
        self.apellido = apellido
        self.registro_medico = registro_medico
        self.malla_citas = []

    def turnosMedicos(nombre):
        hora_actual = datetime.datetime.now()
        entrada = hora_actual.strftime("%H:%M:%S")
        print("Su hora de entrada es: ",entrada)
        hora_sumada = hora_actual + datetime.timedelta(hours=10)
        salida = hora_sumada.strftime("%H:%M:%S")
        print("Doctor",nombre,", el consultorio 100 estará disponible para usted de",entrada,"a",salida)

    #nombre = input("Ingrese su nombre: ")
    #TurnosMedicos(nombre)

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