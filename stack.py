class Stack:
    def _init_(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} onto the stack.")

    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        popped_value = self.top.value
        self.top = self.top.next
        return f"Popped {popped_value} from the stack."

    def is_empty(self):
        return self.top is None

    def peek(self):
        return None if self.is_empty() else self.top.value