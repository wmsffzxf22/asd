class MaxHeap():
    def __init__(self,a):
        self.items = a
        self.size = len(a)
        self.build()

    def heapify(self, i):
        a = self.items
        n = self.size
        l, r = 2 * i + 1, 2 * i + 2
        if l < n and a[l] > a[i]:
            largest = l
        else:
            largest = i
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.heapify(largest)
    def build(self):
        a = self.items
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def maximum(self):
        if self.size<1:
            print('Pusty kopiec')
        else:
            return self.items[0]

    def extract_max(self):
        a = self.items
        n = self.size
        if n < 1:
            print('Pusty kopiec')
        else:
            m = a[0]
            a[0] = a[n-1]
            del a[n-1]
            self.size -= 1
            self.heapify(0)
            return m

    def print(self):
        print(self.items)

    def insert(self,k):
        a = self.items
        a.append(k)
        self.size += 1
        i = self.size - 1
        while i > 0 and a[(i-1)//2] < a[i]:
            a[i], a[(i-1)//2] = a[(i-1)//2], a[i]
            i = (i-1)//2

    def increase_key(self, i, k):
        a = self.items
        if k>a[i]:
            print('Nowy klucz jest mniejszy od aktualnego')
        else:
            a[i] = k
            while i > 0 and a[(i-1)//2] < a[i]:
                a[i], a[(i-1)//2] = a[(i-1)//2], a[i]
                i = (i-1)//2
            
# a = [15,13,9,5,12,8,7,4,0,6,2,1]
# h = MaxHeap(a)
# # h.extract_max()
# h.print()
# h.insert(10)
# h.print()


def isMaxHeap(a):
    for i in range(1,len(a)):
        if a[(i-1)//2] < a[i]:
            return False
    else:
        return True

# a=[23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
# print(a, IsMaxHeap(a)

def max_heapify(a, n, i):
    l, r = 2*i+1, 2*i+2
    if l < n and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, n, largest)


def build_max_heap(a):
    n = len(a)
    for i in range(n//2-1, -1, -1):
        max_heapify(a,n,i)

# a = [5,3,17,10,84,19,6,22,9]
# build_max_heap(a)
# print(a, isMaxHeap(a))

def heapsort(a):
    build_max_heap(a)
    print(a)
    n = len(a)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)
        print(a[:i],' ', a[i:])

# a = [5,3,17,10,84,19,6,22,9]
# print(a)
# heapsort(a)
# print(a)
