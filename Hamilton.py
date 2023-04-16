import random
def macierzSasiedztwa(n,x):
    global Matrix
    Matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        Matrix.append(row)


    xd = x/100
    wNasycenia = ((n*(n-1)/2)*xd)


    gora = []
    for i in range(n):
        for j in range(i+1, n):
            place = []
            place.append(i)
            place.append(j)
            gora.append(place)

    m = n - 1
    while m > 0:
        pog = random.randrange(len(gora))

        if gora[pog][1] == m:
            Matrix[gora[pog][0]][gora[pog][1]] = 1
            Matrix[gora[pog][1]][gora[pog][0]] = 1

            gora.pop(pog)

            wNasycenia -= 1
            m -= 1
            

    while wNasycenia >= 1:
        miejsce = random.randrange(len(gora))
        Matrix[gora[miejsce][0]][gora[miejsce][1]] = 1
        Matrix[gora[miejsce][1]][gora[miejsce][0]] = 1
        gora.pop(miejsce)
        wNasycenia -= 1
    
    print("Macierz Sąsiedztwa:")
    for el in Matrix:
        print(el)

def macierzCykl(n,x):
    global Matrix
    Matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        Matrix.append(row)


    xd = x/100
    wNasycenia = ((n*(n-1)/2)*xd)


    m = n
    vertex = []
    while m > 0:
        vertex.append(m)
        m -= 1


    order = []
    while len(vertex) > 0:
        pog = random.randrange(len(vertex))
        order.append(vertex[pog])
        vertex.pop(pog)

    print(order)


    for i in range(len(order)):
        if (i + 1 >= len(order)):
            Matrix[order[i]-1][order[0]-1] = 1
            Matrix[order[0]-1][order[i]-1] = 1
        else:
            Matrix[order[i]-1][order[i+1]-1] = 1
            Matrix[order[i+1]-1][order[i]-1] = 1
        wNasycenia -= 1


    while (wNasycenia / 3) >= 1:
        nasycanie(0)
        wNasycenia -= 3


    print("Macierz Sąsiedztwa:")
    for el in Matrix:
        print(el)



def macierzBezCyklu(n,x):
    global Matrix
    Matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        Matrix.append(row)


    xd = x/100
    wNasycenia = ((n*(n-1)/2)*xd) + 2


    m = n
    vertex = []
    while m > 0:
        vertex.append(m)
        m -= 1


    order = []
    while len(vertex) > 0:
        pog = random.randrange(len(vertex))
        order.append(vertex[pog])
        vertex.pop(pog)

    print(order)


    for i in range(len(order)):
        if (i + 1 >= len(order)):
            Matrix[order[i]-1][order[0]-1] = 1
            Matrix[order[0]-1][order[i]-1] = 1
        else:
            Matrix[order[i]-1][order[i+1]-1] = 1
            Matrix[order[i+1]-1][order[i]-1] = 1
        wNasycenia -= 1


    for i in range(len(order)):
        if Matrix[i][0] == 1:
            Matrix[i][0] = 0
            Matrix[0][i] = 0


    while (wNasycenia / 3) >= 1:
        nasycanie(1)
        wNasycenia -= 3


    print("Macierz Sąsiedztwa:")
    for el in Matrix:
        print(el)


def Euler(macierz, v):
    for i in range (len(macierz[v])):
        if macierz[v][i]==1:
            macierz[v][i]=0
            macierz[i][v]=0
            Euler(macierz, i)
    S.append(v+1)

def Hamiltonian(path, pos):
    if pos == len(Matrix):
        if Matrix[ path[pos-1]-1 ][ path[0]-1 ] == 1:
            return True
        else:
            return False
    for v in range(1,len(Matrix)):
        if (path.count(v+1)==0)and(Matrix[path[pos-1]-1][v]==1):
            path[pos] = v+1
            if Hamiltonian(path, pos+1) == True:
                return True
            path[pos] = 0
    return False

def Hcycle():
    path = [0] * len(Matrix)
    path[0] = 1
    if Hamiltonian(path,1) == False:
        print ("Nie ma cyklu Hamiltona")
        return False
    else:
        path.append(1)
        print(path)
        return True

def nasycanie(x):
    randVertex = random.randrange(x,n)
    for randVertex2 in range(x, n):
        for randVertex3 in range(x, n):
            if Matrix[randVertex][randVertex2] == 0 and Matrix[randVertex][randVertex3] == 0 and Matrix[randVertex2][randVertex3] == 0 and randVertex != randVertex2 and randVertex != randVertex3 and randVertex2 != randVertex3:
                Matrix[randVertex][randVertex2] = 1
                Matrix[randVertex2][randVertex] = 1

                Matrix[randVertex][randVertex3] = 1
                Matrix[randVertex3][randVertex] = 1
                
                Matrix[randVertex2][randVertex3] = 1 
                Matrix[randVertex3][randVertex2] = 1
                
                print(randVertex+1,randVertex2+1,randVertex3+1)
                return


a = 1
while(a != 0):
    print("1. Wygeneruj graf nieskierowany")
    print("2. Cykl Hamiltona w grafie 30%")
    print("3. Cykl Hamiltona w grafie 70%")
    print("4. Graf nieskierowany, nie-hamiltonowski o nasyceniu 50%")
    print("5. Cykl Eulera w grafie")
    print("6. Cykl Hamiltona w grafie")
    print("0. Zakończ program")
    a = int(input())
    if a == 1:
        print("Podaj n: ")
        n = int(input())
        print("Podaj wspolczynnik nasycenia(np. 60 dla 60%):")
        x = int(input())
        macierzSasiedztwa(n, x)

    if a == 2:
        print("Podaj n:")
        n = int(input())
        x = 30
        macierzCykl(n,x)

    if a == 3:
        print("Podaj n:")
        n = int(input())
        x = 70
        macierzCykl(n,x)       
    
    if a == 4:
        print("Podaj n:")
        n = int(input())
        x = 50
        macierzBezCyklu(n,x)
    if a == 5:
        global S
        S=[]
        x=0
        suma=0
        macierz=[]
        for i in range (len(Matrix)):
            pom=[]
            for j in range (len(Matrix[i])):
                pom.append(Matrix[i][j])
            macierz.append(pom)
            suma+=sum(Matrix[i])
        while (sum(Matrix[x])==0):
            x+=1
        Euler(macierz, x)
        if(len(S)<=suma/2)or(S[0]!=S[len(S)-1]):
            print("Nie ma cyklu Eulera")
        else:
            print(S)
    if a == 6:
        Hcycle()
