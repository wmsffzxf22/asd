def insertion_sort(a):
    t = 0
    for i in range(1, len(a)):
        # print(a[:i],' ',a[i:])
        k = a[i]
        j = i - 1
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
            t += 1
        a[j + 1] = k
        # print('Liczba iteracji while:',t)
    return t

# a=[6,5,4,3,2,1,0]
# print(a)
# print('Liczba nieporzadków:', insertion_sort(a))

def insertion_sort_R(a, n):  # sortuje rekurencyjnie prefiks dlugosci n przez wstawianie
    t = 0
    if n > 1:
        t += insertion_sort_R(a, n - 1)
        k = a[n - 1]
        j = n - 2
        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
            t += 1
        a[j + 1] = k
    return t


a = [6, 2, 4, 3, 2, 1, 0]
print(a)
# insertion_sort_R(a,len(a))
# print(a)
print('Liczba nieporzadków:', insertion_sort_R(a, len(a)))

