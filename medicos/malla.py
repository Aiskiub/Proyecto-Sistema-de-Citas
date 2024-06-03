from datetime import datetime, timedelta


class Malla:
    def __init__(self):
        self.horaInicioJornada = '8:00'  
        self.horaFinJornada = '16:00'  
        self.duracionCitas = '30'  # Duración de cada cita en minutos
        self.malla = {}  # Diccionario para almacenar la malla de horarios
    
    def generarMalla(self):
        franjas = {}  # Diccionario para las franjas horarias disponibles
        fecha = datetime.now()  # Fecha actual
        fechaFin = fecha + timedelta(days=30)  # Fecha final (30 días desde hoy)
        horaFin = datetime.strptime(self.horaFinJornada, '%H:%M')  # Hora de fin de la jornada
        while fecha <= fechaFin:  # Generar malla para los próximos 30 días
            hora = datetime.strptime(self.horaInicioJornada, '%H:%M')  # Hora de inicio de la jornada
            while hora <= horaFin:
                franjas[hora.strftime('%H:%M')] = 'true'  # Marcar la franja horaria como disponible
                hora += timedelta(minutes=float(self.duracionCitas))  # Incrementar la hora según la duración de la cita
            self.malla[(fecha.strftime('%d/%m/%Y'))] = franjas  # Agregar la malla diaria al diccionario
            fecha += timedelta(days=1)  # Pasar al siguiente día
        return self.malla  # Devolver la malla generada