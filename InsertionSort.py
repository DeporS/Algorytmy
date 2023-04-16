import random
import time

times = []

for k in [100, 250, 500, 1000, 5000, 10000, 20000]:
    lista = []
    for i in range(k):
        lista.append(15)
    #print(lista)
    start_time = time.time()
    for i, li in enumerate(lista):
        j = i
        if i == 0:
            pog = 1
        else:
            for k in range(j,0,-1): #do shella -h
                if lista[k] < lista[k-1]:
                    lista[k], lista[k-1] = lista[k-1], lista[k]
                else:
                    break

    times.append(time.time() - start_time)
#print(lista)




#print("--- %s seconds ---" % (time.time() - start_time))
print(times)

