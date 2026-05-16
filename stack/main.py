
class Stack:
    def __init__(self):
        self.stack = []

    @property
    def isEmpty(self):
        return 0 == len(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty:
            return "Pilha esta vazia"

        return self.stack.pop()

    def peek(self):
        if self.isEmpty:
            return "Pilha esta vazia"

        return self.stack[-1]

    def size(self):
        return len(self.stack)


pilha = Stack()

pilha.push("Amanda")
pilha.push("Maria Eduarda")
pilha.push("Venina")
pilha.push("Joao Antonio")
pilha.push("Lilian")

print(f"Tamanho da pilha: {pilha.size()}")

print(f"Ultimo elemento da pilha: {pilha.peek()}")

pilha.pop()

print(f"Ultimo elemento da pilha: {pilha.pop()}")