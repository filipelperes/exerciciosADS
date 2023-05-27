tabela_hash = [[] for i in range(8)]

def funcao_hash(chave):
    return chave % len(tabela_hash)

def insere(tabela_hash, chave, valor):
    linha = funcao_hash(chave)
    tabela_hash[linha].append(valor)

def busca(tabela_hash, chave):
    linha = funcao_hash(chave)
    entrada - tabela_hash[linha]
    for i, chave_valor in enumerate(entrada):
        chave_atual, valor_atual = chave_valor
        if chave == chave_atual:
            return valor_atual