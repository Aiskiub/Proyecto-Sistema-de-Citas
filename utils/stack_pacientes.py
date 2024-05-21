from utils.node import Node

class Stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
        
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            return popped_node.valor
        
    def print_stack(self):
        current = self.top
        while current:
            print(current.valor)
            current = current.next