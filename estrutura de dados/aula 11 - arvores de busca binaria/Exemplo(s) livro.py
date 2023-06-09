class No(object):
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None

class Arvore(object):
    def __init__(self):
        self.raiz = None
        self.cont_espaco = 10

    def insert(self, chave: int) -> None:
        novo = No(chave)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                anterior = atual
                if chave <= atual.chave:
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                else:
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return
                    
    def printTree(self, raiz = None, espaco = 0):
        if (raiz == None):
            return
        espaco += self.cont_espaco
        
        self.printTree(raiz.dir, espaco)
        
        print(end = " " * (espaco - self.cont_espaco))
        print(raiz.chave)
        
        self.printTree(raiz.esq, espaco)
        
    def busca_recursiva(self, chave):
        return self._busca_recursiva(self.raiz, chave)
    
    def _busca_recursiva(self, no: No, chave: int):
        if no != None:
            print("Visitou chave: {}".format(no.chave))
            if no.chave == chave:
                return True
            elif chave <= no.chave:
                return self._busca_recursiva(no.esq, chave)
            elif chave > no.chave:
                return self._busca_recursiva(no.dir, chave)
        return False
        
    def busca_iterativa(self, chave: int):
        return self._busca_iterativa(self.raiz, chave)
    
    def _busca_iterativa(self, no: No, chave: int):
        if no != None:
            no_atual = no
            while no_atual != None:
                print("Visitou Chave: {}".format(no_atual.chave))
                if no_atual.chave == chave:
                    return True
                elif chave <= no_atual.chave:
                    no_atual = no_atual.esq
                else:
                    no_atual = no_atual.dir
    
if __name__ == "__main__":
    lista  = [115, 90, 34, 56, 25, 95, 25, 132, 130, 133]
    testes = [1, 5, 56, 78, 132, 149, 25]
    
    arvore = Arvore()
    buscar = 56
    
    for i in lista:
        arvore.insert(i)
    
    print("Imprimindo a árvore:")
    arvore.printTree(arvore.raiz)
    
    print("\nTrajeto de busca da chave ---> {} - Modo Recursivo\n".format(buscar))
    procura = "Sucesso" if arvore.busca_recursiva(buscar) else "Falha"
    print ("\nResultado da busca: {0}".format(procura))
    
    for teste in testes:
        print("\nChaves percorridas: {0}".format(teste))
        procura = "Sucesso" if arvore.busca_recursiva(teste) else "Falha"
        print ("\nResultado da busca: {0}".format(procura))
    
    for teste in testes:
        print("\nChaves percorridas: {0}".format(teste))
        procura = "Sucesso" if arvore.busca_iterativa(teste) else "Falha"
        print ("\nResultado da busca: {0}".format(procura))