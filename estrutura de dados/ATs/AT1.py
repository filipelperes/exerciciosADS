class Produto:
    def __init__(self, codigo=0, proximo_nodo=None):
        self.codigo=codigo
        self.proximo=proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.codigo, self.proximo)

class ListaEncadeada:
    def __init__(self):
        self.cabeca=None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def addLast(self, item):
        if self.cabeca:
            aux = self.cabeca
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = item
        else:
            self.cabeca = item

lista = ListaEncadeada()

print('Lista vazia: ', lista)

p1 = Produto(1111)
lista.addLast(p1)
print(lista)

p2 = Produto(2222)
lista.addLast(p2)
print(lista)

p3 = Produto(3333)
lista.addLast(p3)
print(lista)