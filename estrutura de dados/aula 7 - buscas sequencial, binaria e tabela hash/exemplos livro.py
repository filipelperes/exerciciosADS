A = [
    ['Mateus', 'Ciências da computação'],
    ['Artur', 'administração']
    ['Juliana', 'Engenharia elétrica'],
    ['Carolina', 'Letras'],
    ['Luana', 'Relações públicas']
]

#Busca sequencial
def busca_sequencial(A, chave, N):
    for i in range(0, N):
        if A[i] == chave:
            return A[i]
    return "Aluno não encontrado!"


chave = input("Digite o nome do aluno p/ pesquisa: ")
N = len(A);

print(busca_sequencial(A, chave, N))


#Busca Binaria
def busca_binaria(A, chave, N):
    esquerda = 0
    direita = N - 1
    while esquerda <= direita:
        meio = int((esquerda + direita) / 2)
        if A[meio] == chave:
            return A[meio]
        elif A[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return "Chave nao encontrada!"


chave = input("Digite o nome do aluno p/ pesquisa: ")
N = len(A);

print(busca_binaria(A, chave, N))


#Funcao HASH para strings
def funcao_hash(chave):
    valor = chave % len(tabela_hash)
    return valor

def insere(tabela_hash, chave, valor):
    linha = funciao_hash(chave)
    chave_existe = False
    entrada = tabela_hash[linha]
    for i, chave_valor in enumerate(entrada):
        chave_atual, valor_atual = chave_valor
        if chave == chave_atual:
            chave_existe = True
            break
        if chave_existe:
            entrada[i] = ((chave, valor))
        else:
            entrada.append((chave, valor))

