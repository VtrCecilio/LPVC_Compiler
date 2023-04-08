namespaces = []

numericos = ['numero', 'operacao_full', 'operacao_operando_unico', 'operacao_paren']
booleanos = ['condicao', 'condicao_unica', 'booleano']

def trata_statements(node):
    statements = node[1:] 
    for statement in statements:
        if statement is not None:
            semantic_analyser(statement)

def trata_root(root):
    node = root[1]
    namespaces.insert(0, {})
    semantic_analyser(node)

def trata_operacao_full(node):
    op1 = semantic_analyser(node[1])
    
    if (op1[0] == 'numero_vazio'):
        print("Erro semântico. Variável '%s' não pode ter valor 'vazio'." % node[1][1])
        exit()
    elif (op1[0] not in numericos):
        print("Erro semântico. Variável '%s' precisa ter tipo 'numero'." % node[1][1])
        exit()

    op2 = semantic_analyser(node[3])
    if (op2[0] == 'numero_vazio'):
        print("Erro semântico. Variável '%s' não pode ter valor 'vazio'." % node[3][1])
        exit()
    elif (op2[0] not in numericos):
        print("Erro semântico. Variável '%s' precisa ter tipo 'numero'." % node[3][1])
        exit()

    if node[4] != None:
        op_resto = semantic_analyser(node[4])
    return node

def trata_operando_unico(node):
    if node[1][0] == 'numero':
            return node[1]
    elif node[1][0] == 'variavel':
        valor_vari = semantic_analyser(node[1])
        if (valor_vari[0] == 'numero') or (valor_vari[0] == 'numero_vazio'):
            return valor_vari
        else:
            print("Erro semântico. Variável '%s' não é numérica." % node[1][1])
            exit()

def trata_numero(node):
    return node

def trata_numero_vazio(node):
    return node

def trata_resto_operacao(node):
    semantic_analyser(node[2])
    return node

def trata_declaracao(node):
    if node[1] in namespaces[0]:
        print("Erro semântico. Variável de identificador '%s' já foi declarada nesse escopo." % node[1])
        exit()
    else:
        valor_node = node[2:][0]
        valor_node = semantic_analyser(valor_node)
        namespaces[0][node[1]] = valor_node
        print(namespaces)

def trata_enquanto(node):
    namespaces.insert(0, {})

def trata_operacao_paren(node):
    print(node)
    semantic_analyser(node[1])
    if node[2] != None:
        semantic_analyser(node[2])
    return node

def trata_atribuicao_numero(node):
    return semantic_analyser(node[1])
        

def trata_variavel(node):
    for namespace in namespaces:
        try:
            vari = namespace[node[1]]
            return vari
        except:
            pass
    print("Erro semântico. Variável '%s' não foi declarada." % node[1])
    exit()


def trata_none(node):
    return None

def trata_atribuicao_texto(node):
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

def trata_atribuicao_booleano(node):
    if node[1][0] in booleanos:
        semantic_analyser(node[1][1])
        semantic_analyser(node[1][3])
        print(node)

def trata_reatribuicao(node):
    variavel = semantic_analyser(('variavel', node[1]))
    
tratamentos = {
    'root' : trata_root,
    'statements' : trata_statements,
    'operacao_full' : trata_operacao_full,
    'operacao_operando_unico' : trata_operando_unico,
    'operacao_paren' : trata_operacao_paren,
    'declaracao' : trata_declaracao,
    'enquanto' : trata_enquanto,
    'atribuicao_numero' : trata_atribuicao_numero,
    'atribuicao_texto' : trata_atribuicao_texto,
    'atribuicao_booleano' : trata_atribuicao_booleano,
    'variavel' : trata_variavel,
    'numero' : trata_numero,
    'numero_vazio' : trata_numero_vazio,
    'resto_operacao' : trata_resto_operacao,
    'reatribuicao' : trata_reatribuicao,
    None : trata_none
}

def semantic_analyser(node):
    funcao_tratar = tratamentos[node[0]]
    return funcao_tratar(node)