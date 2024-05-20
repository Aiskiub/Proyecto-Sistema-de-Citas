from datetime import datetime

class Paciente:
    def __init__(self, nombres, apellidos, tipo_doc, doc_id, fecha_nac):
        self.nombres = nombres
        self.apellidos = apellidos
        self.tipo_doc = tipo_doc
        self.doc_id = doc_id
        self.fecha_nac = fecha_nac
        self.edad = self.calcular_edad()
        self.hist_citas = []
        self.turno = None
        self.clasificacion = self.clasificar_paciente()
        self.cita_asignada = None
    
    def calcular_edad(self):
        hoy = datetime.now()
        fecha_nac = datetime.strptime(self.fecha_nac, "%Y-%m-%d")
        return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
    
    def clasificar_paciente(self):
        edad = self.edad
        if edad < 1:
            return "neonato"
        elif edad < 4:
            return "infante"
        elif edad < 12:
            return "joven"
        elif edad < 18:
            return "joven adulto"
        elif edad < 60:
            return "adulto"
        else:
            return "adulto mayor"
    
    def agregar_cita(self, cita):
        if self.cita_asignada is None:
            self.cita_asignada = cita
            self.hist_citas.append(cita)
            return True
        return False
    
    def cancelar_cita(self):
        self.cita_asignada = None
