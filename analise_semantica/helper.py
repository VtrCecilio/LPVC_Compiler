# Verifica redeclarações apenas no escopo no topo da pilha de namespaces.
def verifica_redeclaracao(id, nms, linha):
    if id in nms[0]:
        print('Erro semântico no statement %d. Variável \'%s\' já foi declarada nesse escopo.' % (linha, id))
        exit()

def verifica_numero(expressao, sa, nms, linha):
    if expressao[0] == 'operacao_binaria':
        verifica_semantica('numero', expressao[1], sa, nms, linha)
        verifica_semantica('numero', expressao[3], sa, nms, linha)
        verifica_semantica('numero', expressao[4], sa, nms, linha)
    elif expressao[0] == 'operacao_parenteses':
        verifica_semantica('numero', expressao[1], sa, nms, linha)
        verifica_semantica('numero', expressao[2], sa, nms, linha)
    elif expressao[0] == 'resto_operacao':
        verifica_semantica('numero', expressao[2], sa, nms, linha)
    else:
        print('Erro semântico no statement %d. Expressão não é do tipo numérica.' % linha)
        exit()

def verifica_texto(expressao, sa, nms, linha):
    if expressao[0] == 'operacao_binaria':
        if expressao[2] != '+':
            print('Erro semântico no statement %d. Tipo \'texto\' não suporta operação \'%s.\'' % (linha, expressao[2]))
            exit()
        else:
            verifica_semantica('texto', expressao[1], sa, nms, linha)
            verifica_semantica('texto', expressao[3], sa, nms, linha)
            verifica_semantica('texto', expressao[4], sa, nms, linha)
    elif expressao[0] == 'operacao_parenteses':
        verifica_semantica('texto', expressao[1], sa, nms, linha)
        verifica_semantica('texto', expressao[2], sa, nms, linha)
    elif expressao[0] == 'resto_operacao':
        if expressao[1] != '+':
            print('Erro semântico no statement %d. Tipo \'texto\' não suporta operação \'%s.\'' % (linha, expressao[1]))
            exit()
        else:
            verifica_semantica('texto', expressao[2], sa, nms, linha)
    else:
        print('Erro semântico no statement %d. Expressão não é do tipo textual.' % linha)
        exit()


def verifica_booleano(expressao, sa, nms, linha):
    if expressao[0] == 'comparacao':
        verifica_semantica('numero', expressao[1], sa, nms, linha)
        verifica_semantica('numero', expressao[3], sa, nms, linha)
    else: 
        print('Erro semântico no statement %d. Expressão não é do tipo booleano.' % linha)
        exit()

def verifica_semantica(tipo, expressao, sa, nms, linha):
    if expressao == None:
        pass
    elif tipo == 'numero':
        if expressao[0] != 'numero':
            verifica_numero(expressao, sa, nms, linha) 
    elif tipo == 'texto':
        if expressao[0] != 'texto':
            verifica_texto(expressao, sa, nms, linha)
    elif tipo == 'booleano':
        if expressao[0] != 'booleano':
            verifica_booleano(expressao, sa, nms, linha)
        