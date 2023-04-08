booleanos1 = ['condicao_unica', 'booleano']
booleanos2 = ['condicao']


def trata_declaracao(node, semantic_analyser, namespaces):
    if node[1] in namespaces[0]:
        print("Erro semântico. Variável de identificador '%s' já foi declarada nesse escopo." % node[1])
        exit()
    else:
        valor_node = node[2:][0]
        valor_node = semantic_analyser(valor_node)
        namespaces[0][node[1]] = valor_node
        print(namespaces)

def trata_variavel(node, semantic_analyser, namespaces):
    for namespace in namespaces:
        try:
            vari = namespace[node[1]]
            return vari
        except:
            pass
    print("Erro semântico. Variável '%s' não foi declarada." % node[1])
    exit()

def trata_atribuicao_numero(node, semantic_analyser, namespaces):
    return semantic_analyser(node[1])

def trata_atribuicao_texto(node, semantic_analyser, namespaces):
    if (node[1][0] == 'texto') or (node[1][0] == 'texto_vazio'):
        return node[1]
    elif (node[1][0] == 'variavel'):
        variavel = trata_variavel(node[1])
        if (variavel[0] == 'texto') or (variavel[0] == 'texto_vazio'):
            return variavel
        else:
            print("Erro semântico. Valor da variável '%s' passada para a atribuição não é do tipo 'texto'." % node[1][1])
            exit()
    exit()

def trata_atribuicao_booleano(node, semantic_analyser, namespaces):
    if node[1][0] in booleanos1:
        semantic_analyser(node[1][1])
    elif node[1][0] in booleanos2:
        semantic_analyser(node[1][3])
    return node[1]

def trata_reatribuicao(node, semantic_analyser, namespaces):
    pass