# from analise_semantica.trata_literais import *
# from analise_semantica.trata_operacoes import *
# from analise_semantica.trata_vari_atri import *
# from analise_semantica.trata_lacos import *

# namespaces = []

# def trata_statements(node, semantic_analyser, namespaces):
#     statements = node[1:] 
#     for statement in statements:
#         if statement is not None:
#             semantic_analyser(statement)

# def trata_root(root, semantic_analyser, namespaces):
#     node = root[1]
#     if node == None:
#         exit()
#     namespaces.insert(0, {})
#     semantic_analyser(node)
        

# tratamentos = {
#     None : trata_none
# }

# def semantic_analyser(node):
#     funcao_tratar = tratamentos[node[0]]
#     return funcao_tratar(node, semantic_analyser, namespaces)