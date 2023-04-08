from trata_literais import *
from trata_operacoes import *
from trata_vari_atri import *
from trata_lacos import *

namespaces = []

def trata_statements(node, semantic_analyser, namespaces):
    statements = node[1:] 
    for statement in statements:
        if statement is not None:
            semantic_analyser(statement)

def trata_root(root, semantic_analyser, namespaces):
    node = root[1]
    namespaces.insert(0, {})
    semantic_analyser(node)
        

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
    'booleano' : trata_booleano,
    'resto_operacao' : trata_resto_operacao,
    'reatribuicao' : trata_reatribuicao,
    None : trata_none
}

def semantic_analyser(node):
    if node[0] == 'root':
        if node[1] == None:
            exit()
    funcao_tratar = tratamentos[node[0]]
    return funcao_tratar(node, semantic_analyser, namespaces)