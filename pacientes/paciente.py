from datetime import date

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
        
# Definimos la clase Paciente
class Paciente:
    def __init__(self, nombre, apellido, tipo_documento, documento_identidad, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_documento = tipo_documento
        self.documento_identidad = documento_identidad
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = calcular_edad(self.fecha_nacimiento)
        self.clasificacion = clasificar(self.edad)
    
    #Getters
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getTipoID(self):
        return self.tipo_id
    def getID(self):
        return self.id
    def getFecha(self):
        return self.fecha_nacimiento
    def getEdad(self):
        return self.edad
    def getHistorial(self):
        return self.historial
    def getCita(self):
        return self.cita
    def getClasificacion(self):
        return self.clasificacion
    
    #Setters
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setTipoID(self, tipo_id):
        self.tipo_id = tipo_id
    def setID(self, id):
        self.id = id
    def setFecha(self, fecha): #Si se cambia la fecha de nacimiento, automáticamente se actualizan los campos de edad y clasificación
        self.fecha_nacimiento = date.fromisoformat(fecha)
        self.edad = calcular_edad(self.fecha_nacimiento)
        self.clasificacion = clasificar(self.edad)
        
        
# Definimos el CRUD   
class GestionDePacientes:
    def __init__(self):
        self.pila_pacientes = []

    def agregar_paciente(self, paciente):
        self.pila_pacientes.append(paciente)
    
    def leer_pacientes(self):
        for paciente in self.pila_pacientes:
            print("Nombre:", paciente.nombre)
            print("Apellido:", paciente.apellido)
            print("Tipo de ID:", paciente.tipo_documento)
            print("Número de ID:", paciente.documento_identidad)
            print("Fecha de Nacimiento:", paciente.fecha_nacimiento)
            print("Edad:", paciente.edad)
            print("Clasificación:", paciente.clasificacion)
            print() 
    
    def eliminar_paciente(self, documento_identidad):
        for i, paciente in enumerate(self.pila_pacientes):
            if paciente.documento_identidad == documento_identidad:
                self.pila_pacientes.pop(i)
                return True
        return False
