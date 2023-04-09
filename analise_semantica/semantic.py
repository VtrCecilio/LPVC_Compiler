from analise_semantica.trata_declaracoes import *

def trata_statements(node, sa, nms, linha):
    statements = node[1:]
    for statement in statements:
        if statement is not None:
            sa(statement, nms, linha + 1)

def trata_root(root, sa, nms, linha):
    node = root[1]
    if node == None:
        exit()
    nms.insert(0, {})
    sa(node, nms, linha)

def trata_none(node, sa, nms):
    pass        

tratamentos = {
    None : trata_none,
    'root' : trata_root,
    'statements' : trata_statements,
    'declaracao' : trata_declaracao
}

def semantic_analyser(node, nms, linha):
    funcao_tratar = tratamentos[node[0]]
    return funcao_tratar(node, semantic_analyser, nms, linha)