class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
        
    def push(self, item): # Metodo para insertar elementos a la pila
        self.items.insert(0, item)
              
    def pop(self): # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop(0)
        
    def print_stack(self): # Metodo para mostrar los elementos de la pila
        print(self.items)