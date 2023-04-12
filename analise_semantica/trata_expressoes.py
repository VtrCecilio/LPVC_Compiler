from analise_semantica.helper import *

def trata_expressoes(node, sa, nms, linha):
    tipo = resolve_type(node, sa, nms, linha)
    verifica_semantica(tipo, node, sa, nms, linha)