from analise_semantica.helper import *

# Laços de repetição
def trata_enquanto(node, sa, nms, linha):
    verifica_semantica('booleano', node[1], sa, nms, linha)
    
    nms.insert(0, {})
    sa(node[2], nms, linha)
    #print(nms[0])
    nms.pop(0)

def trata_para(node, sa, nms, linha):
    verifica_semantica('numero', node[1], sa, nms, linha)
    verifica_semantica('numero', node[2], sa, nms, linha)
    verifica_semantica('numero', node[3], sa, nms, linha)
    nms.insert(0, {})
    sa(node[4], nms, linha)
    nms.pop(0)

# Laço de controle (se | senão)
def trata_se(node, sa, nms, linha):
    verifica_semantica('booleano', node[1], sa, nms, linha)
    
    nms.insert(0, {})
    sa(node[2], nms, linha)
    #print(nms[0])
    nms.pop(0)
    
    nms.insert(0, {})
    sa(node[3], nms, linha)
    #print(nms[0])
    nms.pop(0)