class Queue:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("pop from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)
    
"""                
_init_ inicializa una lista vacía para almacenar los elementos de la cola.
is_empty verifica si la cola está vacía.
push agrega un elemento al final de la cola.
pop elimina y devuelve el primer elemento de la cola.
peek devuelve el primer elemento sin eliminarlo.
size devuelve el número de elementos en la cola.

"cambio 1"
