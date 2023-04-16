# Klasa reprezentujaca pojedynczy wezel drzewa
from ast import Return


class Node:
    def __init__(self, value):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None

#1. Tworzenie drzewa BST
def compare(root, value):
    if value< root.value:
        if root.left is not None:
            compare(root.left, value)
        else:
            root.left = Node(value)
    else:
        if root.right is not None:
            compare(root.right, value)
        else:
            root.right = Node(value)
    return root
def makeBST():
    print("Input number of nodes")
    n=int(input())
    tab=[]
    print("Input node values")
    for i in range (n):
        tab.append(int(input()))
    root=Node(tab[0])
    for i in range(1, n):
        root=compare(root, tab[i])
    return root

#2. Tworzenie drzewa AVL    
def binary(lista, lista2):
    middle = len(lista) // 2    
    lista2.append(lista[middle])
    listaL = lista[:middle]
    listaR = lista[middle + 1:]

    if len(listaL) > 1:
        binary(listaL, lista2)
    elif len(listaL) == 1:
        lista2.append(listaL[0])
    if len(listaR) > 1:
        binary(listaR, lista2)
    elif len(listaR) == 1:
        lista2.append(listaR[0])

def createAVL(root, key):

    if not root:
        return Node(key)
    elif key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def insert( root, key):
    
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root

#3. Wypisanie in-order
def inorder(node):
#kolejność inorder LKP
    if not node:
        return None
    if node.left is not None:
        inorder(node.left)
    print(node.value," ", end='')
    if node.right is not None:
        inorder(node.right)

#4. Wypisanie pre-order
def preorder(node):
#kolejność preorder KLP
    if not node:
        return None
    print(node.value," ", end='')
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)

#5. Usuwanie węzłów
def MinimumValueroot( root):
    if root is None or root.left is None:
        return root
    else:
        return MinimumValueroot(root.left)

def delete(val, root):
    if root is None:
        return root
    elif val < root.value:
        root.left = delete(val, root.left)
    elif val > root.value:
        root.right = delete(val, root.right)
    else:
        if root.left is None:
            left = root.right
            root = None
            return left
        elif root.right is None:
            left = root.left
            root = None
            return left
        right = MinimumValueroot(root.right)
        root.value = right.value
        root.right = delete(right.value, root.right)
    return root
#6. Balansowanie drzewa DSW
def leftrotation(node):
    print(node.value)
    new=node.right
    pom=new.left
    new.left=node
    node.right=pom
    return new
def rightrotation(node):
    new=node.left
    pom=new.right
    new.right=node
    node.left=pom
    return new
def DSW1(node):
    while node.left is not None:
        node=rightrotation(node)
    if node.right is not None:
        node.right=DSW1(node.right)
    return node
def DSW2(node):
    if node.right is not None:
        node=leftrotation(node)
        node.right=DSW2(node.right)
    return node
def DSW3(node):
    if node.right is not None:
        node=leftrotation(node)
        if node.right is not None:
            if node.right.right is not None:
                node.right.right=DSW3(node.right.right)
    return node
def DSW(node):
    node=DSW1(node)
    node=DSW2(node)
    node=DSW3(node)
    return node

#7. Usuwanie całego drzewa
def delpostorder(root):
        if not root:
            return None  
        root.left = delpostorder(root.left)
        root.right = delpostorder(root.right)
        return None

#8. Znajdywanie najmniejszego elementu
def pathmin(node):
    #wypisujemy ścieżkę
    print(node.value, end='')
    if node.left is not None:
        print(" -> ", end='')
        pathmin(node.left)
    else:
        print("")
        #wypisujemy najmniejszy element w nowej linii
        print(node.value, "is the smallest element")

#9. Znajdywanie największego elementu
def pathmax(node):
    #wypisujemy ścieżkę
    print(node.value, end='')
    if node.right is not None:
        print(" -> ", end='')
        pathmax(node.right)
    else:
        print("")
        #wypisujemy największy element w nowej linii
        print(node.value, "is the biggest element")
        
ch='1'
while(ch!='0'):
    print("Choose na option: \n1. Create a BST tree \n2. Create an AVL tree \n3. Print tree in-order \n4. Print tree pre-order \n5. Delete nodes \n6. Balance tree (DSW) \n7. Delete the entire tree \n8. Find smallest element \n9. Find biggest element \n0. End program")
    ch=input()
    if(ch=='1'):
        root=makeBST()
    elif(ch=='2'):
        print("Input node values (for example 1 3 2 5 12): ")
        TreeList = ([int(i) for i in input().split()])
        TreeList.sort()
        ListBinary = []
        binary(TreeList, ListBinary)
        root=Node(ListBinary[0])
        for i in range (1, len(ListBinary)):
            root = createAVL(root, ListBinary[i])
    elif(ch=='3'):
        inorder(root)
        print("")
    elif(ch=='4'):
        preorder(root)
        print("")
    elif(ch=='5'):
        print("Choose how many nodes to delete:")
        num = int(input())
        print("Input node values (for example 1 3 2 5 12): ")
        pog = ([int(i) for i in input().split()])
        for j in pog:
            root=delete(j, root)
    elif(ch=='6'):
        root=DSW(root)
    elif(ch=='7'):
        root=delpostorder(root)
        print("")
    elif(ch=='8'):
        pathmin(root)
        print("")
    elif(ch=='9'):
        pathmax(root)