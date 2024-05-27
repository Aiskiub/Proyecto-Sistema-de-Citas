from datetime import datetime, timedelta

class Medico:
    def __init__(self, nombre, apellido, especialidad, numero_rm, consultorio):
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.numero_rm = numero_rm
        self.citas = []  # Lista para las citas del médico
        self.consultorio = consultorio
    
    def verificar_disponibilidad(self, fecha_programacion, hora_asignacion):
        for cita in self.citas:
            cita_inicio = datetime.combine(cita.fecha_programacion, cita.hora_asignacion)
            cita_fin = cita_inicio + timedelta(minutes=30)
            nueva_cita_inicio = datetime.combine(fecha_programacion, hora_asignacion)
            nueva_cita_fin = nueva_cita_inicio + timedelta(minutes=30)
            
            if not (nueva_cita_fin <= cita_inicio or nueva_cita_inicio >= cita_fin):
                return False
        return True
    
    def ordenar_citas(self):
        self.citas.sort(key=lambda cita: (cita.fecha_programacion, cita.hora_asignacion))
    
    """ MUCHACHOS eso de: lambda cita: (cita.fecha_programacion, cita.hora_asignacion) define una función anónima, 
        la cual toma argumento cita y devuelve una tupla ( o sea 2) (cita.fecha_programacion, cita.hora_asignacion),
        y esa cosa de sort(key=.....) utiliza esta función para extraer "la clave" de ordenamiento de cada cita en la lista self.malla_citas.
        Como resultado, las citas se ordenan primero por fecha_programacion y, en caso de que sea el mismo dia, por hora_asignacion """

    """Si no les gusto podemos poner esta alternativa:
    
    def obtener_clave_orden(cita):
        return (cita.fecha_programacion, cita.hora_asignacion)
    

    def ordenar_citas(self):
        self.citas.sort(key=obtener_clave_orden)"""


    def agregar_cita(self, cita):
        self.citas.append(cita)
        self.ordenar_citas()
    
    def cancelar_cita(self, cita):
        self.citas.remove(cita)
        self.ordenar_citas()

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} ({self.especialidad}), RM: {self.numero_rm}"