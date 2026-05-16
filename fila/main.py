
class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return None

        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return None

        return self.queue[0]

    def size(self):
        return len(self.queue)


fila = Queue()

fila.enqueue("Amanda")
fila.enqueue("Maria Eduarda")
fila.enqueue("Venina")
fila.enqueue("Joao Antonio")
fila.enqueue("Lilian")

print(f"Tamanho da fila: {fila.size()}")

print(f"Primeiro elemento da fila: {fila.peek()}")
