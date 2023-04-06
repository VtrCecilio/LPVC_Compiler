namespaces = []

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
    print(node)
    
def trata_none(node):
    print(node)

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
    pass

def trata_atribuicao_numero(node):
    atri = node[1]
    if atri[0] == 'operacao_operando_unico':
        if atri[1][0] == 'numero':
            return atri[1]
        elif atri[1][0] == 'variavel':
            valor_vari = semantic_analyser(atri[1])
            if (valor_vari[0] == 'numero') or (valor_vari[0] == 'numero_vazio'):
                return valor_vari
            else:
                print("Erro semântico. Variável '%s' não é numérica." % node[1])
    else:
        pass

def trata_variavel(node):
    for namespace in namespaces:
        try:
            vari = namespace[node[1]]
            return vari
        except:
            pass
    print("Erro semântico. Variável '%s' não foi declarada." % node[1])
    exit()
            

def trata_atribuicao_texto(node):
    pass

tratamentos = {
    'root' : trata_root,
    'statements' : trata_statements,
    'operacao_full' : trata_operacao_full,
    'operacao_paren' : trata_operacao_paren,
    'declaracao' : trata_declaracao,
    'enquanto' : trata_enquanto,
    'atribuicao_numero' : trata_atribuicao_numero,
    'atribuicao_texto' : trata_atribuicao_texto,
    'variavel' : trata_variavel,
    None : trata_none
}

def semantic_analyser(node):
    funcao_tratar = tratamentos[node[0]]
    return funcao_tratar(node)