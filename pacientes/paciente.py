from datetime import date

# Calculamos la edad de un paciente a partir de su fecha de nacimiento con ayuda de la librería datetime
def calcular_edad(fecha_nacimiento):
        hoy = date.today()
        if fecha_nacimiento > hoy:
            return hoy.year - fecha_nacimiento.year - 1
        else:
            return hoy.year - fecha_nacimiento.year

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
        
# Definimos la clase Paciente
class Paciente:
    def __init__(self, nombre, apellido, tipo_documento, documento_identidad, fecha_nacimiento, edad=None, historial=None, cita=None, clasificacion=None):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_documento = tipo_documento
        self.documento_identidad = documento_identidad
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = calcular_edad(fecha_nacimiento)
        self.clasificacion = clasificar(edad)


# Definimos el CRUD   
class GestionDePacientes:
    def __init__(self):
        self.pila_pacientes = []

    def agregar_paciente(self, paciente):
        self.pila_pacientes.append(paciente)
        
    def leer_paciente(self, documento_identidad):
        for paciente in self.pila_pacientes:
            if paciente.documento_identidad == documento_identidad:
                return paciente
        return None
    
    def actualizar_paciente(self, documento_identidad, paciente_actualizado):
        for i, paciente in enumerate(self.pila_pacientes):
            if paciente.documento_identidad == documento_identidad:
                self.pila_pacientes[i] = paciente_actualizado
                return True
        return False
    
    def eliminar_paciente(self, documento_identidad):
        for i, paciente in enumerate(self.pila_pacientes):
            if paciente.documento_identidad == documento_identidad:
                self.pila_pacientes.pop(i)
                return True
        return False
    



