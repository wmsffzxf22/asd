def isMaxHeap(a):
    for i in range(1,len(a)):
        if a[(i-1)//2] < a[i]:
            return False
    else:
        return True

# a=[23, 17, 14, 6, 13, 10, 1, 5, 7, 12]
# print(a, IsMaxHeap(a))

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