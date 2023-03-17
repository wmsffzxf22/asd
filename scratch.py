class Stack:
    def __init__(self, vol):  # tworzy nowy stos o pojemności vol
        self.vol = vol
        self.items = [0] * vol
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):  # dodaje element x do stosu self
        if self.size < self.vol:
            self.items[self.size] = x
            self.size += 1
        else:
            print('Przepełnienie stosu')

    def pop(self):  # usuwa element ze stosu self
        if self.size > 0:
            self.size -= 1
            return self.items[self.size]
        else:
            print("Pusty stos")

    def print(self):  # wypisuje elementy stosu
        print(self.items[:self.size])


class Queue:
    def __init__(self, vol):  # tworzy kolejke o pojemności vol
        self.items = [0] * vol
        self.head, self.tail = 0, 0
        self.vol = vol

    def enqueue(self, x):  # dodaje element x do kolejki
        self.items[self.tail] = x
        self.tail += 1

    def dequeue(self):  # usuwa element z kolejki
        x = self.items[self.head]
        self.head += 1
        return x

    def print(self):
        print(self.items[self.head:self.tail])

#2.5
def poprawne(w):
    s = Stack(len(w))
    nawiasy = '()[]{}'
    ot = '([{'
    zam = ')]}'
    za_ot = {')':'(', ']':'[', '}':'{'}
    for x in w:
        if x in ot:
            s.push(x)
        if x in zam:
            if s.is_empty():
                return False
            else:
                y = s.pop()
                if y != za_ot[x]:
                    return False
    return s.is_empty()


# while True:
#     w = input('Podaj wyrażenie: ')
#     if w == 'quit':
#         break
#     if poprawne(w):
#         print('Poprawne')
#     else:
#         print('Niepoprawne')


#2.6
