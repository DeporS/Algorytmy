import random

lista1 = []
for i in range(10):
    lista1.append(random.randrange(1, 10))
print(lista1)

def quickSort(lista, left, right):
    i = left + 1
    j = right
    l = left
    r = right
    pivot = lista[left]
    while i <= j:
        while lista[i] < pivot:
            i += 1
            if i == len(lista):
                break
        while lista[j] > pivot:
            j -= 1
            if j == 0:
                break
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
            #print(lista)
    lista[j], lista[left] = lista[left], lista[j]
    print(lista)
    if i == j:
        quickSort(lista, l, j - 1)
        quickSort(lista, j+1, r)
    if i > j:
        quickSort(lista, l, j)
        quickSort(lista, j, r)
quickSort(lista1, 0, 9)





