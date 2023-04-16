import enum
import random
import time




lista = []
k = 10000
for i in range(k):
    lista.append(random.randrange(0,k))
#print(lista)
start_time = time.time()
for i, val in enumerate(lista):
    k = i
    minVal = lista[i]
    for j in range(i+1, len(lista)):
        if lista[j] < minVal:
            minVal = lista[j]
            k = j
    lista[i], lista[k] = lista[k], lista[i]
    #print(lista)
#print(lista)    

#if i <= k/2:
#    lista.append(i)
#else:
#    lista.append(k-i)
print("--- %s seconds ---" % (time.time() - start_time))