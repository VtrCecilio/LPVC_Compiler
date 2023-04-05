namespaces = []

def trata_statements(node):
    statements = node[1:] 
    for statement in statements:
        if statement is not None:
            semantic_analyser(statement)

def trata_root(root):
    node = root[1]
    namespaces.append(dict)
    semantic_analyser(node)

def trata_operacao_full(node):
    print(node)
    
def trata_none(node):
    print(node)

def trata_declaracao(node):
    print(node)

def trata_enquanto(node):
    namespaces.append(dict)

    

tratamentos = {
    'root' : trata_root,
    'statements' : trata_statements,
    'operacao_full' : trata_operacao_full,
    'declaracao' : trata_declaracao,
    'enquanto' : trata_enquanto,
    None : trata_none
}

def semantic_analyser(node):
    funcao_tratar = tratamentos[node[0]]
    funcao_tratar(node)