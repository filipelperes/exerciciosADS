class No:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
    def getData(self):
        return self.label
    def setData(self, data):
        self.label = data
    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left
    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    #Insere informação
    def insert(self, number):
        #Cria um novo no 
        node = Node(number)

        #Verifica se a arvore esta vazia
        if self.isEmpty():
            self.root = node
        else:
            #Árvore não vazia
            curr_node = self.root
            dad_node = None
            while True:
                if curr_node != None:
                    #Verifica se vai para esquerda ou direita
                    if node.getLabel() == curr_node.getLabel():
                        curr_node = curr_node.getLeft() #Prossegue a esquerda
                    else:
                        curr_node = curr_node.getRight() #Prossegue a direita
                else:
                    #Se curr_node é None, então encontrou onde inserir
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node) #Insere a esquerda
                    else:
                        dad_node.setRight(node) #Insere a direita
                break

    #Verifica se a arvore esta vazia
    def isEmpty(self):

    #Mostra em pré-ordem
    def preOrder(self):

    #Mostra em ordem
    def inOrder(self):

    #Mostra em pos-ordem
    def postOrder(self):

    #Método sucessor
    def noSucessor(self, noRemove): #O parametro é a referencia para o nó que deseja-se remover
        dadSucessor = None
        successor = noRemove
        curr_node = noRemove.right #Vai para a subárvore a direita
        while curr_node != None: #Enquanto não chegar no Nó mais a esquerda
            dadSucessor = successor
            successor = curr_node
            curr_node = curr_node.left #Caminha para a esquerda
            if successor != no_remove.right: #Se sucessor não é o filho a direita do Nó a ser eliminado
                dadSucessor.left = successor.right #Pai herda os filhos do sucessor
                successor.right = no_remove.right #Guardando a referencia a direita do sucessor
                return successor

    #Remove nó
    def remove(self, number):
        if self.root == None:
            return False #Se arvore vazia
        curr_node = self.root
        dad = self.root
        child_left = True
        #Busca a posição do número
        while curr_node.getLabel() != number: #Enquanto não encontrou
            dad = curr_node
        if number < curr_node.getLabel(): #Caminha para esquerda
            curr_node = curr_node.getLeft()
            child_left = True #É filho a esquerda? sim
        else: #Caminha para direita
            curr_node = curr_node.getRight()
            child_left = False #É filho a direita? NAO
        if curr_node == None:
            return False #Encontrou uma folha, então sai do laço
        """
        Caso 1
        Se não possui nenhum filho (é uma folha), elimine-o
        """
        if curr_node.getLeft() == None and curr_node.getRight() == None:
            if curr_node == self.root:
                self.root = None #Se raiz

            else:
                if child_left:
                    dad.left = None #Se for filho a esquerda do pai

                else:
                    dad.right = None #Se for filho a direita do pai
        """
        Caso 2
        Se o nó a ser removido possui um filho a esquerda
        """
        if curr_node.getLeft() != None:
            if child_left:
                dad.left = curr_node.left #Se for filho a esquerda

            else:
                dad.right = curr_node.left #Se for filho a direita

        #Se o nó a ser removido possui um filho a direita
        elif curr_node.right != None:
            if child_left:
                dad.left = curr_node.right #Se for filho a esquerda

            else:
                dad.right = curr_node.right #Se for filho a direita
        """
        Caso 3
        Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
        """
        sucessor = self.noSucessor(curr_node)
        #Usando sucessor que seria o Nó mais a esquerda da subarvore a direita
        if child_left:
            dad.left = sucessor #Se for filho a esquerda do pai
        else:
            dad.right = sucessor #Se for filho a direita do pai
        sucessor.left = curr_node.left #Acertando o ponteiro a esqueda do sucessor
        #Agora que ele assumiu a posição correta na árvore
        return True


    #Busca informação
    def search(self, number):
        #Verifica se a arvore esta vazia
        if self.isEmpty():
            print("Árvore vazia")
        else:
            #Árvore não está vazia, busca numero
            curr_node = self.root
            while True:
                if curr_node.getLabel() == number:
                    print("O dado foi encontrado na árvore")
                    break
                elif number < curr_node.getLabel():
                    curr_node = curr_node.getLeft() #Continua a esquerda
                else:
                    curr_node = curr_node.getRight() #Continua a direita

    #Recebe o endereço do nó raiz
    def getRoot(self):

    #Busca o maior valor
    def bigger(self):