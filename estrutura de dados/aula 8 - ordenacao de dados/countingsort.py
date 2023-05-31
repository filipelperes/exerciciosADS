def countingSort(lista, N):
    #Vetores auxiliares
    saida = [None] * N
    contador = [None] * (max(lista) + 1)

    #Contador p/ inicializar o '0'
    for i in range(0, max(lista) + 1):
        contador[i] = 0

    #Calculo do numero de vezxes que o numero aparece na lista
    for i in range(0, N):
        contador[lista[i]] = contador[lista[i]] + 1

    #Soma total dos valores
    for i in range(1, max(lista) + 1):
        contador[i] = contador[i] + contador[i - 1]

    #Posições corretas
    for i in range(0, N):
        saida[contador[lista[i]] - 1] = lista[i]
        contador[lista[i]] = contador[lista[i]] - 1

    #Vetor de saida e original resultando na lista ordenada
    for i in range(0, N):
        lista[i] = saida[i]