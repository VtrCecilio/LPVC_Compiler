from analise_semantica.helper import *

def trata_imprima(node, sa, nms, linha):
    if node[1][0] not in literais:
        if node[1][0] == 'variavel':
            variavel = busca_namespaces(node[1][1], nms, linha)
        else:
            tipo = resolve_type(node[1], sa, nms, linha)
            verifica_semantica(tipo, node[1], sa, nms, linha)

def trata_leia(node, sa, nms, linha):
    if node[1][0] != 'variavel':
        print('Erro semântico. Parâmetro da função \'leia\' precisa ser uma (e apenas uma) variável, que já foi declarada.')
        exit()
    else:
        variavel, indice = busca_namespaces(node[1][1], nms, linha)