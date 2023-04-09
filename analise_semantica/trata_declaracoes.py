from analise_semantica.helper import *

def trata_declaracao(node, sa, nms, linha):
    tipo = node[1]
    id = node[2]
    expressao = node[3]
    verifica_redeclaracao(id, nms, linha)
    verifica_semantica(tipo, expressao, sa, nms, linha)    

    nms[0][id] = (tipo, expressao)


# def trata_variavel(node):
#     for namespace in namespaces:
#         try:
#             vari = namespace[node[1]]
#             return vari
#         except:
#             pass
#     print("Erro semântico. Variável '%s' não foi declarada." % node[1])
#     exit()

# def trata_atribuicao_numero(node):
#     return semantic_analyser(node[1])

# def trata_atribuicao_texto(node):
#     if (node[1][0] == 'texto') or (node[1][0] == 'texto_vazio'):
#         return node[1]
#     elif (node[1][0] == 'variavel'):
#         variavel = trata_variavel(node[1])
#         if (variavel[0] == 'texto') or (variavel[0] == 'texto_vazio'):
#             return variavel
#         else:
#             print("Erro semântico. Valor da variável '%s' passada para a atribuição não é do tipo 'texto'." % node[1][1])
#             exit()
#     exit()

# def trata_atribuicao_booleano(node):
#     if node[1][0] in booleanos1:
#         semantic_analyser(node[1][1])
#     elif node[1][0] in booleanos2:
#         semantic_analyser(node[1][3])
#     return node[1]

# def trata_reatribuicao(node):
#     pass