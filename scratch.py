class Stack:
    def __init_(self, vol): #tworzy nowy stos o pojemności vol
        self.items = [0] * vol
        self.size = 0
        self.vol = vol

    def push(self, x): #dodaje element x do stosu self
        if self.size < self.vol:
            self.items[self.size] = x
            self.size += 1
        else:
            print('Przepełnienie stosu')

    def pop(self): # usuwa element ze stosu self
        if self.size > 0:
            self.size -= 1
            return self.items[self.size]
        else:
            print("Pusty stos")

    def print(self): #wypisuje elementy stosu
        print(self.items[:self.size])

class Queue:
    def __init__(self, vol): # tworzy kolejke o pojemności vol
        self.items = [0] * vol
        self.head, self.tail = 0, 0
        self.vol = vol

    def enqueue(self, x): #dodaje element x do kolejki
        self.items[self.tail] = x
        self.tail += 1

    def dequeue(self): #usuwa element z kolejki
        x = self.items[self.head]
        self.head += 1
        return x
    
    def print(self):
        print(self.items[self.head:self.tail])
