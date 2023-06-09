class NoArvore(object):
    def __init__(self, item):
        self.item = item
        self.esq = None
        self.dir = None

# Implementação em busca pós ordem
def pos_order(atual):
    if atual != None:
        pos_order(atual.esq)
        pos_order(atual.dir)
        print(atual.item, end=' ')

# Implementação em busca em pré ordem
def pre_order(atual):
    if atual != None:
        print(atual.item, end=' ')
        pre_order(atual.esq)
        pre_order(atual.dir)

def printTree(raiz, space):
    if (raiz == None):
        return
    space += 10
    printTree(raiz.dir, space)
    print(end = " " * (space - 10))
    print(raiz.item)
    printTree(raiz.esq, space)


# Implementação em busca em ordem
def in_order(atual):
    if atual != None:
        in_order(atual.esq)
        print(atual.item, end = " ")
        in_order(atual.dir)

if __name__ == '__main__':
    arvore = NoArvore('A')

    arvore.esq = NoArvore('B')
    arvore.dir = NoArvore('C')

    arvore.esq.esq = NoArvore('D')
    arvore.esq.dir = NoArvore('E')
    arvore.dir.esq = NoArvore('F')
    arvore.dir.dir = NoArvore('G')

    arvore.esq.esq.esq = NoArvore('H')
    arvore.esq.esq.dir = NoArvore('I')
    arvore.esq.dir.esq = NoArvore('J')
    arvore.esq.dir.dir = NoArvore('K')
    arvore.dir.esq.esq = NoArvore('L')
    arvore.dir.esq.dir = NoArvore('M')
    arvore.dir.dir.esq = NoArvore('N')
    arvore.dir.dir.dir = NoArvore('O')

    print('Imprime a árvore: \n')
    printTree(arvore, 0)
    print('\n')

    print('Pós ordem: ')
    pos_order(arvore)
    print('\n')

    print('Pré ordem: ')
    pre_order(arvore)
    print('\n')

    print('Em ordem: ')
    in_order(arvore)
    print('\n')