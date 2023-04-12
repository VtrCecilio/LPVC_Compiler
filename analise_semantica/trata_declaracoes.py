from analise_semantica.helper import *

# Declaração de variáveis
def trata_declaracao(node, sa, nms, linha):
    tipo = node[1]
    id = node[2]
    expressao = node[3]
    verifica_redeclaracao(id, nms, linha)
    verifica_semantica(tipo, expressao, sa, nms, linha)    

    nms[0][id] = (tipo, expressao)


def trata_reatribuicao(node, sa , nms, linha):
    varivavel, i = busca_namespaces(node[1], nms, linha)
    verifica_semantica(varivavel[0], node[2], sa, nms, linha)

    nms[i][node[1]] = node[2] 


# Declaração de procedimentos
def trata_procedimento(node, sa, nms, lina):
    pass