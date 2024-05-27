from utils.stack import Stack

class GestionDePacientes:
    def __init__(self):
        self.pila_pacientes = Stack()  # Cambiamos la lista por una pila
        
    def agregar_paciente(self, paciente):
        self.pila_pacientes.push(paciente)
    
    def leer_pacientes(self):
        pacientes = []
        current_node = self.pila_pacientes.top
        while current_node is not None:
            paciente = current_node.valor
            pacientes.append(paciente)
            current_node = current_node.next
        
        if not pacientes:
            print("No hay pacientes en la pila.")
        return pacientes
    
    def buscar_paciente(self, documento_identidad):
        current_node = self.pila_pacientes.top
        while current_node is not None:
            if current_node.valor.documento_identidad == documento_identidad:
                return current_node.valor
            current_node = current_node.next
        return None
    
    def borrar_paciente(self, documento_identidad):
        current_node = self.pila_pacientes.top
        prev_node = None
        while current_node is not None:
            if current_node.valor.documento_identidad == documento_identidad:
                if prev_node is None:
                    self.pila_pacientes.pop()  # Eliminar el primer elemento de la pila
                else:
                    prev_node.next = current_node.next  # Saltar el nodo actual
                return True
            prev_node = current_node
            current_node = current_node.next
        return False
    
    def actualizar_paciente(self, documentoBuscado, campo, nuevoValor):
        current_node = self.pila_pacientes.top
        found = False
        while current_node is not None:
            if current_node.valor.documento_identidad == documentoBuscado:
                setattr(current_node.valor, campo, nuevoValor)
                found = True
                break
        if found == False:
            print("No se encontró ningún paciente con ese documento de identidad.")
        

''' def actualizar_pacientes(self, documento_identidad, nuevo_nombre, nuevo_apellido):
        current_node = self.pila_pacientes.top
        while current_node is not None:
            if current_node.valor.documento_identidad == documento_identidad:
                current_node.valor.nombre = nuevo_nombre
                current_node.valor.apellido = nuevo_apellido
                return True
            current_node = current_node.next
        return False'''
