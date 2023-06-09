class No:
    def __init__(self, item):
        self.item = item
        self.esq = None
        self.dir = None

def inOrder(raiz, inorder):
    if raiz is None:
        return
    inOrder(raiz.esq, inorder)
    inorder.append(raiz.item)
    inOrder(raiz.dir, inorder)

def contaNo(raiz):
    if raiz is None:
        return 0
    return contaNo(raiz.esq) + contaNo(raiz.dir) + 1

def arrToBST(arr, raiz):
    if raiz is None:
        return
    arrToBST(arr, raiz.esq)
    raiz.item = arr[0]
    arr.pop(0)
    arrToBST(arr, raiz.dir)

def convert(raiz):
    if raiz is None:
        return
    n = contaNo(raiz)
    arr = []
    inOrder(raiz, arr)
    arr.sort()

def printTree(raiz, espaco = 0):
    cont_espaco = 10
    if (raiz == None):
        return

    espaco += cont_espaco

    printTree(raiz.dir, espaco)
    
    print(end = " " * (espaco - cont-espaco))
    print(raiz.item)
    
    printTree(raiz.esq, espaco)
    
raiz = No(10)
raiz.esq = No(2)
raiz.dir = No(7)
raiz.esq.esq = No(8)
raiz.esq.dir = No(4)

convert(raiz)
print('Árvore convertida')
printTree(raiz)