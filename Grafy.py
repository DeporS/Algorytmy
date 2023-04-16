import random

# Definiowanie macierzy sasiedztwa
def macierzSasiedztwa(n):
    # Tworzenie globalnej tablicy Matrix
    global Matrix
    Matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        Matrix.append(row)
    # Ustalanie wspolczynnika nasycenia
    wNasycenia = ((n*(n-1)/2)/2)
    # Stworzenie tablicy z kordynatami gornej czesci macierzy
    gora = []
    for i in range(n):
        for j in range(i+1, n):
            place = []
            place.append(i)
            place.append(j)
            gora.append(place)
    # Dodanie do macierzy jedynek w losowo wygenerowanych miejscach
    m = n - 1
    while m > 0:
        pog = random.randrange(len(gora))
        if gora[pog][1] == m:
            Matrix[gora[pog][0]][gora[pog][1]] = 1
            gora.pop(pog)
            wNasycenia -= 1
            m -= 1
    while wNasycenia >= 1:
        miejsce = random.randrange(len(gora))
        Matrix[gora[miejsce][0]][gora[miejsce][1]] = 1
        gora.pop(miejsce)
        wNasycenia -= 1
    
    # Zaprezentowanie macierzy w przejrzysty sposob
    print("Macierz Sąsiedztwa:")
    for el in Matrix:
        print(el)

# Definiowanie macierzy sasiedztwa pobieranej z klawiatury
def macierzSasiedztwaKlawiatura():

    print("Podaj liczbę wierszy: ")
    num = int(input())
    # Tworzenie globalnej listy Matrix ktora uzytkownik musi uzupelnic
    global Matrix
    Matrix = []
    print("Podaj wiersze np. '0 1 1 0'")
    while num > 0:       
        wiersz = list(map(int, input().split()))
        num -= 1
        Matrix.append(wiersz)
    
    # Zaprezentowanie macierzy w przejrzysty sposob
    print("Macierz Sąsiedztwa:")
    for el in Matrix:
        print(el)

# Definiowanie listy nastepnikow
def listaNastepnikow():
    # Utworzenie globalnej listy na podstawie juz istniejacej macierzy
    global Lista
    Lista = []
    for i in range(len(Matrix)):
        pom=[]
        for j in range(len(Matrix[i])):
            if Matrix[i][j]==1:
                pom.append(j+1)
        Lista.append(pom)

    # Zaprezentowanie listy nastepnikow w przejrzysty sposob
    print("Lista Następników:")
    for i in range(len(Lista)):
        print(Lista[i])

# Definiowanie tabeli krawedzi
def tabelaKrawedzi():
    # Utworzenie globalnej tabeli na podstawie juz istniejacej macierzy
    global Tabela
    Tabela=[]
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            if Matrix[i][j]==1:
                Tabela.append([i+1, j+1])

    # Zaprezentowanie tabeli krawedzi w przejrzysty sposob
    print("Tabela Krawędzi:")
    for i in range(len(Tabela)):
        print(Tabela[i])

# Wypisanie wierzcholkow grafu w kolejnosci DFS bazujac na macierzy
def DFSmacierz(x):
    print("Wierzchołki w kolejności DFS:")
    # Utworzenie listy zawierajacej deklaracje wierzcholkow grafu
    visited=[0]*size
    # Utworzenie stacku ktory bedzie zapamietywal nasza droge po grafie
    stack=[]
    # Wybranie pierwszego wierzcholka
    visited[x]=1
    stack.append(x)
    while (visited.count(0)>0) or len(stack)>0:
       if len(stack)==0:
           for i in range (len(visited)):
               if visited[i]==0:
                    # Zaznaczenie wierzcholka w ktorym jestesmy oraz dodanie go do stacku
                   visited[i]=1
                   stack.insert(0,i)
                   break
        # Po zakonczeniu wypisujemy pierwszy wierzcholek ze stacku a pozniej go usuwamy
       x=stack.pop(0)
       print(x+1, end= " ")
       for i in range (len(Matrix[x])):
           if Matrix[x][i]==1:
            if visited[i]==0:
                visited[i]=1
                stack.insert(0,i)

    print('')

# Wypisanie wierzcholkow grafu w kolejnosci DFS bazujac na liscie nastepnikow
def DFSlista(x):
    print("Wierzchołki w kolejności DFS:")
    # Utworzenie listy zawierajacej deklaracje wierzcholkow grafu
    visited=[0]*size
    # Utworzenie stacku ktory bedzie zapamietywal nasza droge po grafie
    stack=[]
    # Wybranie pierwszego wierzcholka
    visited[x]=1
    stack.append(x)
    while (visited.count(0)>0) or len(stack)>0:
       if len(stack)==0:
           for i in range (len(visited)):
               if visited[i]==0:
                    # Zaznaczenie wierzcholka w ktorym jestesmy oraz dodanie go do stacku
                   visited[i]=1
                   stack.insert(0,i)
                   break
        # Po zakonczeniu wypisujemy pierwszy wierzcholek ze stacku a pozniej go usuwamy
       x=stack.pop(0)
       print(x+1, end= " ")
       for i in range (len(Lista[x])):
        q=Lista[x][i]-1
        if visited[q]==0:
            visited[q]=1
            stack.insert(0,q)
    print('')  

# Wypisanie wierzcholkow grafu w kolejnosci DFS bazujac na tabeli krawedzi
def DFStabela(x):
    print("Wierzchołki w kolejności DFS:")
    # Utworzenie listy zawierajacej deklaracje wierzcholkow grafu
    visited=[0]*size
    # Utworzenie stacku ktory bedzie zapamietywal nasza droge po grafie
    stack=[]
    # Wybranie pierwszego wierzcholka
    visited[x]=1
    stack.append(x)
    while (visited.count(0)>0) or len(stack)>0:
        if len(stack)==0:
            for i in range (len(visited)):
                if visited[i]==0:
                    # Zaznaczenie wierzcholka w ktorym jestesmy oraz dodanie go do stacku
                    visited[i]=1
                    stack.insert(0,i)
                    break
        # Po zakonczeniu wypisujemy pierwszy wierzcholek ze stacku a pozniej go usuwamy
        x=stack.pop(0)
        print(x+1, end= " ")
        i=0
        while(i<len(Tabela)):
            if(Tabela[i][0]==x+1):
                q=Tabela[i][1]-1
                if visited[q]==0:
                    visited[q]=1
                    stack.insert(0,q)
            i+=1
    print('') 

# Wypisanie wierzcholkow grafu w kolejnosci BFS bazujac na macierzy
def BFSmacierz(x):
    print("Wierzchołki w kolejności BFS:")
    # Utworzenie listy zawierajacej deklaracje wierzcholkow grafu
    visited=[0]*size
    # Utworzenie kolejki
    queue=[]
    # Wybranie pierwszego wierzcholka
    visited[x]=1
    queue.append(x)
    # Petla wypisujaca wierzcholki
    while (visited.count(0)>0) or len(queue)>0:
       if len(queue)==0:
           for i in range (len(visited)):
               if visited[i]==0:
                   visited[i]=1
                   queue.append(i)
                   break
       x=queue.pop(0)
       print(x+1, end= " ")
       for i in range (len(Matrix[x])):
           if Matrix[x][i]==1:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
    print('')  

# Wypisanie wierzcholkow grafu w kolejnosci BFS bazujac na liscie nastepnikow
def BFSlista(x):
    print("Wierzchołki w kolejności BFS:")
    # Utworzenie listy zawierajacej deklaracje wierzcholkow grafu
    visited=[0]*size
    # Utworzenie kolejki
    queue=[]
    # Wybranie pierwszego wierzcholka
    visited[x]=1
    queue.append(x)
    # Petla wypisujaca wierzcholki
    while (visited.count(0)>0) or len(queue)>0:
       if len(queue)==0:
           for i in range (len(visited)):
               if visited[i]==0:
                   visited[i]=1
                   queue.append(i)
                   break
       x=queue.pop(0)
       print(x+1, end= " ")
       for i in range (len(Lista[x])):
        q=Lista[x][i]-1
        if visited[q]==0:
            visited[q]=1
            queue.append(q)
    print('')  

# Wypisanie wierzcholkow grafu w kolejnosci BFS bazujac na tabeli krawedzi
def BFStabela(x):
    print("Wierzchołki w kolejności BFS:")
    # Utworzenie listy zawierajacej deklaracje wierzcholkow grafu
    visited=[0]*size
    # Utworzenie kolejki
    queue=[]
    # Wybranie pierwszego wierzcholka
    visited[x]=1
    queue.append(x)
    # Petla wypisujaca wierzcholki
    while (visited.count(0)>0) or len(queue)>0:
        if len(queue)==0:
            for i in range (len(visited)):
                if visited[i]==0:
                    visited[i]=1
                    queue.append(i)
                    break
        x=queue.pop(0)
        print(x+1, end= " ")
        i=0
        while(i<len(Tabela)):
            if(Tabela[i][0]==x+1):
                q=Tabela[i][1]-1
                if visited[q]==0:
                    visited[q]=1
                    queue.append(q)
            i+=1
    print('')  

# Sortowanie topologiczne macierzy w kolejnosci DFS
def topoDFSmacierz():
    print("Wierzchołki w kolejności DFS:")
    visited=[0]*size
    stack=[]
    pom=[]
    while (visited.count(0)>0) or len(stack)>0:
        if len(stack)==0:
            for i in range (len(visited)):
                if visited[i]==0:
                    visited[i]=1
                    stack.insert(0,i)
                    break
        x=stack[0]
        for i in range (len(Matrix[x])):
            if Matrix[x][i]==1:
                if visited[i]==0:
                    visited[i]=1
                    stack.insert(0,i)
        if(x==stack[0]):
           pom.append(stack.pop(0)+1)
           visited[x]=1
    for i in range(size-1, -1, -1):
        print(pom[i], end=" ")
    print("")

# Sortowanie topologiczne listy w kolejnosci DFS
def topoDFSlista():
    print("Wierzchołki w kolejności DFS:")
    visited=[0]*size
    stack=[]
    pom=[]
    while (visited.count(0)>0) or len(stack)>0:
        if len(stack)==0:
            for i in range (len(visited)):
                if visited[i]==0:
                    visited[i]=1
                    stack.insert(0,i)
                    break
        x=stack[0]
        for i in range (len(Lista[x])):
            q=Lista[x][i]-1
            if visited[q]==0:
                visited[q]=1
                stack.insert(0,q)
        if(x==stack[0]):
           pom.append(stack.pop(0)+1)
           visited[x]=1
    for i in range(size-1, -1, -1):
        print(pom[i], end=" ")
    print("")

# Sortowanie topologiczne tabeli w kolejnosci DFS
def topoDFStabela():
    print("Wierzchołki w kolejności DFS:")
    visited=[0]*size
    stack=[]
    pom=[]
    while (visited.count(0)>0) or len(stack)>0:
        if len(stack)==0:
            for i in range (len(visited)):
                if visited[i]==0:
                    visited[i]=1
                    stack.insert(0,i)
                    break
        x=stack[0]
        i=0
        while(i<len(Tabela)):
            if(Tabela[i][0]==x+1):
                q=Tabela[i][1]-1
                if visited[q]==0:
                    visited[q]=1
                    stack.insert(0,q)
            i+=1
        if(x==stack[0]):
           pom.append(stack.pop(0)+1)
           visited[x]=1
    for i in range(size-1, -1, -1):
        print(pom[i], end=" ")
    print("")

# Sortowanie topologiczne macierzy w kolejnosci BFS
def topoBFSmacierz():
    print("Graf posortowany topologicznie:")
    poprzedniki=[0]*size
    visited=[0]*size
    for j in range(size):
        for i in range (size):
            poprzedniki[j]+=Matrix[i][j]
    while(visited.count(0)>0):
        i=0
        while(poprzedniki[i]>0) or (visited[i]>0):
            i+=1
        visited[i]=1
        print(i+1, end=' ')
        for j in range(size):
            poprzedniki[j]-=Matrix[i][j]
    print('')

# Sortowanie topologiczne listy w kolejnosci BFS
def topoBFSlista():
    print("Graf posortowany topologicznie:")
    poprzedniki=[0]*size
    visited=[0]*size
    for i in range(size):
        for j in range (len(Lista[i])):
            poprzedniki[Lista[i][j]-1]+=1
    while(visited.count(0)>0):
        i=0
        while(poprzedniki[i]>0) or (visited[i]>0):
            i+=1
        visited[i]=1
        print(i+1, end=' ')
        for j in range(len(Lista[i])):
            poprzedniki[Lista[i][j]-1]-=1
    print('')

# Sortowanie topologiczne tabeli w kolejnosci BFS
def topoBFStabela():
    print("Graf posortowany topologicznie:")
    poprzedniki=[0]*size
    visited=[0]*size
    for i in range (len(Tabela)):
        poprzedniki[Tabela[i][1]-1]+=1
    while(visited.count(0)>0):
        i=0
        while(poprzedniki[i]>0) or (visited[i]>0):
            i+=1
        visited[i]=1
        print(i+1, end=' ')
        for j in range(len(Tabela)):
            if(Tabela[j][0]-1==i):
                poprzedniki[Tabela[j][1]-1]-=1
    print('')

# Menu wyboru
a = -1
while(a != 0):
    print("1. Wygeneruj graf")
    print("2. Przeszukiwanie w głąb")
    print("3. Przeszukiwanie wszerz")
    print("4. Sortowanie topologiczne w głąb")
    print("5. Sortowanie topologiczne wszerz")
    print("0. Zakończ program")
    a = int(input())
    if a == 1:
        # Generowanie grafu
        print("1. Wypełnij losowo")
        print("2. Podaj wiersze z klawiatury")
        b = int(input())
        if b == 1:
            # Losowe wypelnienie
            print("Podaj n: ")
            n = int(input())
            macierzSasiedztwa(n)
        elif b == 2:
            # Wypelnienie z klawiatury
            macierzSasiedztwaKlawiatura()
        # Tworzenie listy oraz tabeli na podstawie juz stworzonej macierzy
        listaNastepnikow()
        tabelaKrawedzi()
        size=len(Matrix)
    elif a == 2:
        # Przeszukiwanie w glab wedlug wybranych parametrow
        print("1. Na bazie macierzy sąsiedztwa")
        print("2. Na bazie listy następników")
        print("3. Na bazie tabeli krawędzi")
        b=int(input())
        print("Podaj numer wierzchołka startowego, lub 0 by zacząć od losowego wierzchołka")
        c=int(input())
        if c==0:
            c=random.randint(1, size)
        if b==1:
            DFSmacierz(c-1)
        elif b==2:
            DFSlista(c-1)
        elif b==3:
            DFStabela(c-1)
    elif a==3:
        # Przeszukiwanie wszerz wedlug wybranych parametrow
        print("1. Na bazie macierzy sąsiedztwa")
        print("2. Na bazie listy następników")
        print("3. Na bazie tabeli krawędzi")
        b=int(input())
        print("Podaj numer wierzchołka startowego, lub 0 by zacząć od losowego wierzchołka")
        c=int(input())
        if c==0:
            c=random.randint(1, size)
        if b==1:
            BFSmacierz(c-1)
        elif b==2:
            BFSlista(c-1)
        elif b==3:
            BFStabela(c-1)
    elif a==4:
        # Sortowanie topologiczne w glab
        print("1. Na bazie macierzy sąsiedztwa")
        print("2. Na bazie listy następników")
        print("3. Na bazie tabeli krawędzi")
        b=int(input())
        if b==1:
            topoDFSmacierz()
        elif b==2:
            topoDFSlista()
        elif b==3:
            topoDFStabela()
    elif a==5:
        # Sortowanie topologiczne wszerz
        print("1. Na bazie macierzy sąsiedztwa")
        print("2. Na bazie listy następników")
        print("3. Na bazie tabeli krawędzi")
        b=int(input())
        if b==1:
            topoBFSmacierz()
        elif b==2:
            topoBFSlista()
        elif b==3:
            topoBFStabela()
