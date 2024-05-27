from datetime import datetime, timedelta

class Malla:
    def __init__(self):
        self.horaInicioJornada = '8:00'
        self.horaFinJornada = '16:00'
        self.duracionCitas = '30'
        self.malla = {}
    
    def generarMalla(self):
        franjas = ()
        fecha = datetime.now()
        fechaFin = fecha + timedelta(days=30)
        horaFin = datetime.strptime(self.horaFinJornada, '%H:%M')
        while fecha <= fechaFin:
            hora = datetime.strptime(self.horaInicioJornada, '%H:%M')
            while hora <= horaFin:
                franjas+=hora.strftime('%H:%M'),
                hora += timedelta(minutes=float(self.duracionCitas))
            self.malla[(fecha.strftime('%d/%m/%Y'))] = franjas
            fecha += timedelta(days= 1)
        return self.malla
            
    
    

    