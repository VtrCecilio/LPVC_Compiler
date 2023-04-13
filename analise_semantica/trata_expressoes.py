from analise_semantica.helper import *

def trata_expressoes(node, sa, nms, linha):
    tipo = resolve_type(node, sa, nms, linha)
    verifica_semantica(tipo, node, sa, nms, linha)

def trata_chama_procedimento(node, sa, nms, linha):
    procedimento, i = busca_procedimento(node[1], nms, linha)
    if (node[2] == None) and len(procedimento['argumentos']) > 0:
        print('Erro semântico no statement %d. Procedimento \'%s\' necessita de \'%d\' argumentos.' % (linha, node[1], len(procedimento['argumentos'])))
        exit()
    elif (node[2] == None) and len(procedimento['argumentos'] == 0):
        pass
    else:
        verifica_parametros(node[2], procedimento['argumentos'], sa, nms, linha)

    return procedimento['tipo']