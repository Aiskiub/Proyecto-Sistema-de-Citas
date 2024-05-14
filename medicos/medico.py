import datetime

def TurnosMedicos(nombre):
    hora_actual = datetime.datetime.now()
    entrada = hora_actual.strftime("%H:%M:%S")
    print("Su hora de entrada es: ",entrada)
    hora_sumada = hora_actual + datetime.timedelta(hours=10)
    salida = hora_sumada.strftime("%H:%M:%S")
    print("Doctor",nombre,", el consultorio 100 estará disponible para usted de",entrada,"a",salida)

nombre = input("Ingrese su nombre: ")
TurnosMedicos(nombre)





