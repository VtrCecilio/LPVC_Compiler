from analise_semantica.helper import *

def trata_expressoes(node, sa, nms, linha):
    tipo = resolve_type(node, sa, nms, linha)
    verifica_semantica(tipo, node, sa, nms, linha)

def trata_chama_procedimento(node, sa, nms, linha):
    procedimento, i = busca_procedimento(node[1], nms, linha)
    n_parametros = conta_parametros(node[2])
    if n_parametros != len(procedimento['argumentos']):
        print('Erro semântico no statement %d. Procedimento \'%s\' necessita de \'%d\' argumentos, foram passados \'%d\'.' % (linha, node[1], len(procedimento['argumentos']), n_parametros))
        exit()
    else:
        verifica_parametros(node[2], procedimento['argumentos'], sa, nms, linha)

    return procedimento['tipo']