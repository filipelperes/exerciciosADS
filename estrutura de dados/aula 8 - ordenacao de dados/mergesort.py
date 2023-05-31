# Ordenação por mistura
def merge_sort(lista, esq, dir):
    if(esq < dir):
        meio = (esq + dir) // 2
        merge_sort(lista, esq, meio)
        merge_sort(lista, meio + 1, dir)
        merge(lista, esq, meio, dir)

def merge(lista, esq, meio, dir):
    v = [None] * (dir - esq + 1)
    i = esq
    j = meio + 1
    k = 0
    while(i <= meio and j <= dir):
        if(lista[i] <= lista[j]):
            lista[k] = lista[i]
            i += 1
        else:
            lista[k] = lista[j]
            j += 1
        k += 1
    while(i <= meio):
        lista[k] = lista[i]
        i += 1
        k += 1
    while(j <= dir):
        lista[k] = lista[j]
        j += 1
        k += 1
    for i in range(0, k):
        lista[esq + i] = v[i]