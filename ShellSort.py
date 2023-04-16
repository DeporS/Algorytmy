import random
import time

times = []

for k in [100, 250, 500, 1000, 5000, 10000]:
    lista = []
    for i in range(k):
        lista.append(random.randrange(0,k))
    #print(lista)
    start_time = time.time()

    h = len(lista) // 2

    while h >= 1:
        for i in range(h, len(lista)):
            ele = lista[i]
            j = i
            while j >= h and lista[j - h] > ele:
                lista[j] = lista[j - h]
                j -= h

            lista[j] = ele
        #print(lista, h)
        h //= 2
        
        




    times.append(time.time() - start_time)
    #print(lista)
    print(all(lista[i] <= lista[i+1] for i in range(len(lista) - 1)))

print(times)
