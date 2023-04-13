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
def trata_procedimento(node, sa, nms, linha):
    verifica_redeclaracao_procedimento(node[1], nms, linha)
    nms.insert(0, {'procedimento' : {}})
    nms[1]['procedimento'][node[1]] = {'tipo' : node[3], 'argumentos' : []}
    inicializa_argumentos(node[2], node[1], sa, nms, linha)
    sa(node[4], nms, linha)
    verifica_semantica(node[3], node[5], sa, nms, linha)
    nms.pop(0)