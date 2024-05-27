from datetime import datetime, timedelta

class Malla:
    def __init__(self, duracion) -> None:
        fechaInicio = datetime.now()
        fechaFin = fechaInicio + datetime.timedelta(days=30)
        horaInicio = '8:00'
        horaFin = '4:00'
        duracion = datetime.strptime(duracion, '%M')
        franjas = []
    
    def generarFranjas(self):
        fecha = self.fechaInicio
        horaFin = datetime.strptime(self.horaFin, '%H:%M')
        while fecha <= self.fechaFin:
            hora = datetime.strptime(self.horaInicio, '%H:%M')
            while hora <= horaFin:
                self.franjas.append(datetime.combine(fecha, hora))
                hora += timedelta(minutes= self.duracion)

