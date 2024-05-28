from datetime import date
from utils.stack import Stack
   
# Definimos la clase Paciente
class Paciente:
    def __init__(self, nombre, apellido, tipo_documento, documento_identidad, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_documento = tipo_documento
        self.documento_identidad = documento_identidad
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = self.calcular_edad(self.fecha_nacimiento)
        self.clasificacion = self.clasificar(self.edad)
        self.cita = None
        self.tiene_cita = False

    # Calculamos la edad de un paciente a partir de su fecha de nacimiento con ayuda de la librería datetime
    def calcular_edad(fecha_nacimiento):
        fecha_actual = date.today()
        resultado = fecha_actual.year - fecha_nacimiento.year
        resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return resultado
    
    # Clasificamos la edad de un paciente en función de su edad
    def clasificar(edad):
        if edad is None:
            return "Edad desconocida"
        if edad >= 0 and edad < 1:
            return "neonato"
        elif edad >= 1 and edad < 12:
            return "infante"
        elif edad >= 12 and edad < 18:
            return "joven"
        elif edad>=18 and edad <40:
            return "joven adulto"   
        elif edad>=40 and edad<60:
            return "adulto"
        elif edad >=60 and edad<120:
            return "adulto mayor"
        else:
            return "Edad no clasificada"
   