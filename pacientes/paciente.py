from datetime import date

def calcular_edad(fecha_nacimiento):
        hoy = date.today()
        if fecha_nacimiento > hoy:
            return hoy.year - fecha_nacimiento.year - 1
        else:
            return hoy.year - fecha_nacimiento.year
        
def clasificar(edad):
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
        return None
        
class Paciente:
    def __init__(self, nombre, apellido, tipo_documento, documento_identidad, fecha_nacimiento, edad=None, historial=None, cita=None, clasificacion=None):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_documento = tipo_documento
        self.documento_identidad = documento_identidad
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = calcular_edad(fecha_nacimiento)
        
        self.clasificacion = clasificar(edad)
        
    

