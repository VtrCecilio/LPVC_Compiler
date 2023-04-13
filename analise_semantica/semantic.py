from analise_semantica.trata_declaracoes import *
from analise_semantica.trata_funcoes import *
from analise_semantica.trata_lacos import *
from analise_semantica.trata_expressoes import *
from analise_semantica.helper import literais, operacoes

# Trata statements em ordem (Por exemplo dado o nó Root ou em um laço)
def trata_statements(node, sa, nms, linha):
    statements = node[1:]
    for statement in statements:
        if (statement != None) and (statement[0] in literais):
            # Apenas um literal, o statement já é considerado correto por si só
            pass
        elif (statement != None) and (statement[0] in operacoes):
            trata_expressoes(statement, sa, nms, linha)
        else:
            sa(statement, nms, linha)
        linha += 1


# Trata o primeiro nó da AST
def trata_root(root, sa, nms, linha):
    node = root[1]
    if node == None:
        exit()
    nms.insert(0, {'procedimento' : {}})
    sa(node, nms, linha)

# Trata o fim de um statement ou statments
def trata_none(node, sa, nms, linha):
    pass        


# Mapeamento de nó -> função_de_tratamento
tratamentos = {
    None : trata_none,
    'root' : trata_root,
    'statements' : trata_statements,
    'declaracao' : trata_declaracao,
    'reatribuicao' : trata_reatribuicao, 
    'imprima' : trata_imprima,
    'leia' : trata_leia,
    'enquanto' : trata_enquanto,
    'se' : trata_se,
    'para' : trata_para,
    'procedimento' : trata_procedimento,
    'chama_procedimento' : trata_chama_procedimento,
}


# Analisa semanticamente statements que não são só expressões
def semantic_analyser(node, nms, linha):
    
    if node != None:
        funcao_tratar = tratamentos[node[0]]
    else:
        funcao_tratar = tratamentos[node]
    return funcao_tratar(node, semantic_analyser, nms, linha)