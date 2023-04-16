def Dynamic():
    file = open("content.txt", "r")
    capacity = int(file.readline())
    weight = []
    value = []
    n = int(file.readline())
    for i in range(n):
        both = file.readline().strip()
        a = both.split(" ")
        value.append(int(a[0]))
        weight.append(int(a[1]))
    #print(value, weight)
    file.close()
    matrix = []
    for j in range(n+1):
        matrix2 = []
        for i in range(capacity+1):
            matrix2.append(0)
        matrix.append(matrix2)
   
    
    for i in range(1,n+1):
        for j in range(0,capacity+1):
            #print(i, j)
            if j - weight[i-1] < 0:
                matrix[i][j] = matrix[i-1][j]
            elif matrix[i-1][j] > (matrix[i-1][j-weight[i-1]] + value[i-1]):
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j-weight[i-1]] + value[i-1]
    
    a = capacity
    b = n
    inside = []

    print("")

    for i in range(n+1):
        print(matrix[i])


    print("")

    for i in range(n):
        if matrix[b][a] == matrix[b-1][a]:
            print("Element " + str(b) + " nie nalezy do plecaka")
            b = b - 1
        else:
            print("Element " + str(b) + " nalezy do plecaka")
            inside.append(b)
            b = b - 1
            a = a - weight[b]
            
    print("")

    print("Najbardziej optymalne rozwiazanie: ")
    inside.sort()
    print(inside)

    print("")

pog = 10
while pog != 0:
    print("Wybierz zadanie")
    print("1. Dynamicznie")
    print("2. ")

    print("")
    print("0. Koniec programu")
    pog = int(input())
    if pog == 1:
        Dynamic()
    elif pog == 2:
        pog = 2
    elif pog == 0:
        break
            
