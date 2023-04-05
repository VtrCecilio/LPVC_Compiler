def trata_statements(node):
    statements = node[1:] 
    for statement in statements:
        if statement is not None:
            semantic_analyser(statement)

def trata_root(root):
    node = root[1]
    semantic_analyser(node)

def trata_operacao_full(node):
    pass

def trata_none():
    pass

tratamentos = {
    'root' : trata_root,
    'statements' : trata_statements,
    'operacao_full' : trata_operacao_full,
    None : trata_none
}

def semantic_analyser(node):
    funcao_tratar = tratamentos[node[0]]
    funcao_tratar(node)