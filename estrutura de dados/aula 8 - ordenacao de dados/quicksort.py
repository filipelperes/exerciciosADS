# Ordenação rapida
# Exemplo video
def quickSort(lista, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quickSort(lista, inicio, p-1)
        quickSort(lista, p+1, fim)

def partition(lista, inicio0, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


# Exemplo livro
def quicksort(lista, esq, dir):
    if esq < dir:
        indice = particao(lista, esq, dir)
        quicksort(lista, esq, indice-1)
        quicksort(lista, indice+1, dir)

def particao(lista, esq, dir):
    pivo = lista[dir]
    i = esq
    for j in range(esq, dir):
        if lista[j] <= pivo:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[dir] = lista[dir], lista[i]
    return i