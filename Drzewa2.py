from csv import list_dialects
from tkinter.tix import Tree

#Dodanie tej klasy obiektu
class treeroot(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

do = ""
TreeList = []
main_root = None

#metoda połowienia binarnego
def binary(lista, lista2):
    middle = len(lista) // 2    
    lista2.append(lista[middle])
    listaL = lista[:middle]
    listaR = lista[middle + 1:]
    #print(listaL, listaR)
    if len(listaL) > 1:
        binary(listaL, lista2)
    elif len(listaL) == 1:
        lista2.append(listaL[0])
    if len(listaR) > 1:
        binary(listaR, lista2)
    elif len(listaR) == 1:
        lista2.append(listaR[0])

#Klasa Drzewa
class AVLTree(object):

    #Tworzenie drzewa
    def create(self, root, key):

        if not root:
            return treeroot(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        return root

    #Dodawanie elementow
    def insert(self, root, key):
    
        if not root:
            return treeroot(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        b = self.getBal(root)

        if b > 1 and key < root.left.value:
            return self.rRotate(root)

        if b < -1 and key > root.right.value:
            return self.lRotate(root)

        if b > 1 and key > root.left.value:
            root.left = self.lRotate(root.left)
            return self.rRotate(root)

        if b < -1 and key < root.right.value:
            root.right = self.rRotate(root.right)
            return self.lRotate(root)

        return root

    #Lewa rotacja
    def lRotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    #Prawa rotacja
    def rRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    #Otrzymanie wysokosci
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    #Sprawdzanie balansu
    def getBal(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    #Najmniejsza wartosc w drzewie
    def MinimumValueroot(self, root):
        if root is None or root.left is None:
            return root
        else:
            return self.MinimumValueroot(root.left)

    #Wypisanie preorder
    def preorder(self, root):

        if not root:
            return
        print(root.value, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    #Wypisanie inorder
    def inorder(self, root):
        if not root:
            return       
        self.inorder(root.left)        
        print(root.value, end=' ')    
        self.inorder(root.right)

    #Wypisanie sciezki do najmniejszego elementu
    def smallestValue(self, root):
        print(root.value, end="")
        if not root.left:
            print("")
            return
        print(" -> ", end=" ")
        self.smallestValue(root.left)

    #Wypisanie sciezki do najwiekszego elementu
    def highestValue(self, root):
        print(root.value, end="")
        if not root.right:
            print("")
            return
        print(" -> ", end=" ")
        self.highestValue(root.right)

    #Usuwanie drewa postorder
    def delpostorder(self, root):
        if not root:
            return None  
        root.left = self.delpostorder(root.left)
        root.right = self.delpostorder(root.right)
        return None

    #Usuwanie elementow
    def delete(self, val, root):
        if root is None:
            return root
        elif val < root.value:
            root.left = self.delete(val, root.left)
        elif val > root.value:
            root.right = self.delete(val, root.right)
        else:
            if root.left is None:
                left = root.right
                root = None
                return left
            elif root.right is None:
                left = root.left
                root = None
                return left
            right = self.MinimumValueroot(root.right)
            root.value = right.value
            root.right = self.delete(right.value, root.right)
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        getBal = self.getBal(root)
        if getBal > 1 and self.getBal(root.left) >= 0:
            return self.rRotate(root)
        if getBal < -1 and self.getBal(root.right) <= 0:
            return self.lRotate(root)
        if getBal > 1 and self.getBal(root.left) < 0:
            root.left = self.lRotate(root.left)
            return self.rRotate(root)
        if getBal < -1 and self.getBal(root.right) > 0:
            root.right = self.rRotate(root.right)
            return self.lRotate(root)
        return root

    #Szkic drzewa
    def sketch(self, root):
        print(root.value)

while(1):
    print("")
    print("Wybierz jedna z opcji:")
    print("")
    print("1. Stworzenie drzewa")
    print("2. Wypisanie drzewa pre-order") 
    print("3. Wypisanie drzewa in-order")
    print("4. Najmniejsza wartosc i jej sciezka")
    print("5. Najwieksza wartosc i jej sciezka")
    print("6. Usuniecie całego drzewa element po elemencie (post-order)")
    print("7. Usuniecie elementow drzewa") 
    #print("8. Dodanie elementu do drzewa") 
    #print("9. Wyswietl szkic drzewa")

    print("0. Wyłącz program")
    print("")
    do = int(input())
    if do == 1:
        print("Podaj wartosci, ktore chcesz dodac do drzewa(np. 1 3 2 5 12): ")
        TreeList = ([int(i) for i in input().split()])
        TreeList.sort()
        treeson = AVLTree()
        ListBinary = []
        binary(TreeList, ListBinary)
        #print(ListBinary)
        for i in ListBinary:
            main_root = treeson.create(main_root, i)
            #print(i)



    elif do == 2:
        treeson.preorder(main_root)
    elif do == 3:
        treeson.inorder(main_root)
    elif do == 4:
        treeson.smallestValue(main_root)
    elif do == 5:
        treeson.highestValue(main_root)
    elif do == 6:
        main_root = treeson.delpostorder(main_root)
    elif do == 7:
        print("Wybierz ilosc wartosc do usuniecia:")
        num = int(input())
        print("Wybierz wartosci do usuniecia (np. 3 2 5 12):")
        pog = ([int(i) for i in input().split()])
        for j in pog:
            treeson.delete(j, main_root)
    #elif do == 8:
    #    print("Podaj wartosc ktora chcesz dodac do drzewa:")
    #    add = int(input())
    #    main_root = treeson.insert(main_root, add)
    #elif do == 9:
    #    treeson.sketch(main_root)
    elif do == 0:
        break