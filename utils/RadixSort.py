from datetime import datetime
from citas.cita import Cita

# Esta función de Counting Sort es para ordenar citas basado en un dígito específico
def counting_sort_citas(citas, exp):
    n = len(citas)  # numero de citas en la lista
    output = [0] * n  # Array de salida que contendrá las citas ordenadas
    count = [0] * 10  # Array de conteo para almacenar el conteo de dígitos (0-9)

    # contar la frecuencia de los dígitos en la posición actual (exp)
    for i in range(n):
        index = citas[i].fecha_programacion.strftime("%Y%m%d%H%M")  # Convertir la fecha y hora a una cadena de dígitos
        count[(int(index) // exp) % 10] += 1  # Incrementar el conteo del dígito correspondiente

    # es para cambiar count[i] para que contenga la posición actual de este dígito en output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # construir el array de salida
    i = n - 1
    while i >= 0:
        index = citas[i].fecha_programacion.strftime("%Y%m%d%H%M")  # convertir la fecha y hora a una cadena de dígitos
        output[count[(int(index) // exp) % 10] - 1] = citas[i]  # colocar la cita en su posición ordenada :D
        count[(int(index) // exp) % 10] -= 1  # Decrementar el conteo para el dígito correspondiente
        i -= 1

    # Copiar el array de salida o sea el output(que tiene la nueva info) a citas[], para que ahora contenga los elementos ordenados
    for i in range(n):
        citas[i] = output[i]

# Función principal de Radix Sort para ordenar citas por fecha y hora
def radix_sort_citas(citas):
    if not citas:  # Verificar si la lista de citas está vacía
        return

    # Encontrar la cita con la fecha y hora más alta para determinar el número máximo de dígitos
    max_fecha = max(citas, key=lambda cita: cita.fecha_programacion).fecha_programacion.strftime("%Y%m%d%H%M")
    max_num = int(max_fecha)  # Convertir la fecha y hora más alta a un número entero

    exp = 1  # Inicializar exp a 1 (representando las unidades)
    # Aplicar Counting Sort para cada dígito (exp = 1, 10, 100, ...)
    while max_num // exp > 0:
        counting_sort_citas(citas, exp)
        exp *= 10  # Moverse al siguiente dígito más significativo

""" En el algoritmo, 'exp' representa la posición del dígito que estamos considerando en la fecha y hora de cada cita. 
Comenzamos con el dígito menos significativo (las unidades de minutos) y avanzamos hacia la izquierda para considerar 
los dígitos de las decenas de minutos, horas, días, meses y años. Usamos 'exp' para organizar las citas en grupos 
basados en el valor de esos dígitos y luego las ordenamos dentro de esos grupos para obtener la lista de citas 
ordenadas por fecha y hora. """