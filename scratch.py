class Stack:
    def __init_(self, vol): #tworzy nowy stos o pojemności vol
        self.items = [0] * vol
        self.size = 0

    def push(self, x): #dodaje element x do stosu self
        self.items[self.size] = x
        self.size += 1

    def pop(self): # usuwa element ze stosu self
        self.size -= 1
        return self.items[self.size]

    def print(self): #wypisuje elementy stosu
        print(self.items[:self.size])

#s = Stack(10)
#s.push('d')
#s.push('h')
#s.pop()
#s.push('f')
#s.push('s')
#s.pop()
#s.pop()
#s.push('m')
#print(s.items)
#print(s.items[:s.size])
#
#
#inny stos
#s = Stack(5)
#s.print()
#s.push('a')
#s.print()
#s.pop()
#s.print()
#for x in 'bsgf':
#   s.push(x)
#
#s.print()
#s.pop()
#s.pop()
#s.push('k')
#s.print()
#
#inne stosy
#s1 = Stack(5)
#s2 = Stack(5)
#s3 = Stack(5)
#for x in 'abcd'
#   s1.push(x)
#s1.print()
#s2.push(s1.pop())
#s2.print()
#s3.push(s1.pop())
#s3.print()
#s1.print()
#


