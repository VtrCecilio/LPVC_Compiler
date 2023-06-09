from analise_semantica.helper import *

# Laços de repetição

    # Laço WHILE
def trata_enquanto(node, sa, nms, linha):
    verifica_semantica('booleano', node[1], sa, nms, linha)
    
    nms.insert(0, {'procedimento' : {}})
    sa(node[2], nms, linha)
    #print(nms[0])
    nms.pop(0)

    # Laço FOR
def trata_para(node, sa, nms, linha):
    verifica_semantica('numero', node[1], sa, nms, linha)
    verifica_semantica('numero', node[2], sa, nms, linha)
    verifica_semantica('numero', node[3], sa, nms, linha)
    nms.insert(0, {'procedimento' : {}})
    sa(node[4], nms, linha)
    nms.pop(0)

# Laço de controle condicional

    # Laço SE
def trata_se(node, sa, nms, linha):
    verifica_semantica('booleano', node[1], sa, nms, linha)
    
    # Semantica dos statements do SE
    nms.insert(0, {'procedimento' : {}})
    sa(node[2], nms, linha)
    #print(nms[0])
    nms.pop(0)
    
    # Semantica dos statements do SENAO
    nms.insert(0, {'procedimento' : {}})
    sa(node[3], nms, linha)
    #print(nms[0])
    nms.pop(0)