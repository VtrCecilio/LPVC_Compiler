from analise_semantica.semantic import semantic_analyser, namespaces

numericos = ['numero', 'operacao_full', 'operacao_operando_unico', 'operacao_paren']

def trata_operacao_full(node):
    op1 = semantic_analyser(node[1])
    
    if (op1[0] == 'numero_vazio'):
        print("Erro semântico. Variável '%s' não pode ter valor 'vazio'." % node[1][1])
        exit()
    elif (op1[0] not in numericos):
        print("Erro semântico. Variável '%s' precisa ter tipo 'numero'." % node[1][1])
        exit()

    op2 = semantic_analyser(node[3])
    if (op2[0] == 'numero_vazio'):
        print("Erro semântico. Variável '%s' não pode ter valor 'vazio'." % node[3][1])
        exit()
    elif (op2[0] not in numericos):
        print("Erro semântico. Variável '%s' precisa ter tipo 'numero'." % node[3][1])
        exit()

    if node[4] != None:
        op_resto = semantic_analyser(node[4])
    return node

def trata_operacao_paren(node):
    print(node)
    semantic_analyser(node[1])
    if node[2] != None:
        semantic_analyser(node[2])
    return node

def trata_operando_unico(node):
    if node[1][0] == 'numero':
            return node[1]
    elif node[1][0] == 'variavel':
        valor_vari = semantic_analyser(node[1])
        if (valor_vari[0] == 'numero'):
            return valor_vari
        elif (valor_vari[0] == 'numero_vazio'):
            print("Erro semântico. Variável '%s' é numérica mas tem valor 'vazio'." % node[1][1])
            exit()
        else:
            print("Erro semântico. Variável '%s' não é numérica." % node[1][1])
            exit()

def trata_resto_operacao(node):
    semantic_analyser(node[2])
    return node