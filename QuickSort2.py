import random
import time


start_time = time.time()


lista = []
k = 100
for i in range(k):
    lista.append(random.randrange(0,k))

print(lista)
#quicksort zmiana indeksow, z lewej i prawej

def quickSort(x, l, p):
    if l<p:
        pivot = x[0]
        #print(pivot)
        i = l
        j = p
        while i <= j:
            while x[j] > pivot:
                j -= 1
            while x[i] < pivot:
                i += 1
            if i <= j:
                x[j],x[i] = x[i], x[j]
                i += 1
                j -= 1
            if i == j:
                quickSort(x, l, i-1)
                quickSort(x, i+1, p)
            if i > j:
                quickSort(x, l ,i)
                quickSort(x, i, p)
        #print(x)


        #left.append(x[i])
        #return left + right


print(quickSort(lista, 0, len(lista)-1))
#quickSort(lista)
print("--- %s seconds ---" % (time.time() - start_time))