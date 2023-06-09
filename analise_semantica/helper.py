literais = ['texto', 'numero', 'booleano']
operacoes = ['operacao_binaria', 'operacao_parenteses', 'comparacao']

# Verifica redeclarações apenas no escopo no topo da pilha de namespaces
def busca_namespaces(id, nms, linha):
    i = 0
    for nm in nms:
        if id in nm:
            return nm[id], i
        i += 1
    print('Erro semântico no statement %d. Variável \'%s\' não foi declarada.' % (linha, id))
    exit()

def busca_procedimento(id, nms, linha):
    i = 0
    for nm in nms:
        if id in nm['procedimento']:
            return nm['procedimento'][id], i
        i += 1
    print('Erro semântico no statement %d. Procedimento \'%s\' não foi declarado.' % (linha, id))
    exit()

# Verifica em uma declaração se a variável/procedimento já foi declarada no escopo atual
def verifica_redeclaracao(id, nms, linha):
    if id in nms[0]:
        print('Erro semântico no statement %d. Variável \'%s\' já foi declarada nesse escopo.' % (linha, id))
        exit()

def verifica_redeclaracao_argumento(id, nms, linha):
    if id in nms[0]:
        print('Erro semântico no statement %d. Argumento com identificador \'%s\' já foi mencionado.' % (linha, id))
        exit()

def verifica_redeclaracao_procedimento(id, nms, linha):
    if id in nms[0]['procedimento']:
        print('Erro semântico no statement %d. Procedimento \'%s\' já foi declarada nesse escopo.' % (linha, id))
        exit()


# Subfunção de verifica_semantica (Numero)
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
    elif expressao[0] == 'variavel':
        variavel, i = busca_namespaces(expressao[1], nms, linha)
        verifica_semantica('numero', variavel, sa, nms, linha)
    elif expressao[0] == 'chama_procedimento':
        procedimento, i = busca_procedimento(expressao[1], nms, linha)
        if procedimento['tipo'] != 'numero':
            print('Erro semântico no statement %d. Procedimento %s não retorna tipo \'numero\'.' % (linha, expressao[1]))
            exit()
    else:
        print('Erro semântico no statement %d. Expressão não é do tipo numérica.' % linha)
        exit()


# Subfunção de verifica_semantica (Texto)
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
    elif expressao[0] == 'variavel':
        variavel, i = busca_namespaces(expressao[1], nms, linha)
        verifica_semantica('texto', variavel, sa, nms, linha)
    elif expressao[0] == 'chama_procedimento':
        procedimento, i = busca_procedimento(expressao[1], nms, linha)
        if procedimento['tipo'] != 'texto':
            print('Erro semântico no statement %d. Procedimento %s não retorna tipo \'texto\'.' % (linha, expressao[1]))
            exit()
    else:
        print('Erro semântico no statement %d. Expressão não é do tipo textual.' % linha)
        exit()


# Subfunção de verifica_semantica (Booleano)
def verifica_booleano(expressao, sa, nms, linha):
    if expressao[0] == 'comparacao':
        verifica_semantica('numero', expressao[1], sa, nms, linha)
        verifica_semantica('numero', expressao[3], sa, nms, linha)
    elif expressao[0] == 'variavel':
        variavel, i = busca_namespaces(expressao[1], nms, linha)
        verifica_semantica('booleano', variavel, sa, nms, linha)

    elif expressao[0] == 'chama_procedimento':
        procedimento, i = busca_procedimento(expressao[1], nms, linha)
        if procedimento['tipo'] != 'booleano':
            print('Erro semântico no statement %d. Procedimento %s não retorna tipo \'booleano\'.' % (linha, expressao[1]))
            exit()
    else: 
        print('Erro semântico no statement %d. Expressão não é do tipo booleano.' % linha)
        exit()


# Verifica a validade semântica de uma expressão
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


# Descobre o tipo de uma operação com base no primeiro operando
def resolve_type(node, sa, nms, linha):
    if node[0] in literais:
        return node[0]
    elif node[0] == 'comparacao':
        return 'booleano'
    elif node[0] == 'variavel':
        variavel, index = busca_namespaces(node[1], nms, linha)
        return variavel[0]
    else:
        return resolve_type(node[1], sa, nms, linha)


# Inicializa argumentos no namespace de uma função
def inicializa_argumentos(argumentos, proc_id, sa, nms, linha):
    argumento1 = argumentos[0]

    verifica_redeclaracao_argumento(argumento1[1], nms, linha)

    resto_argumentos = argumentos[1]
    if argumento1[0] == 'numero':
        nms[0][argumento1[1]] = ('numero', 0)
    elif argumento1[0] == 'texto':
        nms[0][argumento1[1]] = ('texto', '')
    elif argumento1[0] == 'booleano':
        nms[0][argumento1[1]] = ('booleano', 'verdadeiro')

    nms[1]['procedimento'][proc_id]['argumentos'].append(argumento1[0]) 

    if resto_argumentos != None:
        inicializa_argumentos(resto_argumentos, proc_id, sa, nms, linha)

def verifica_parametros(parametros, argumentos, sa, nms, linha):
    
    if parametros != None:
        tipo_parametro1 = resolve_type(parametros[0], sa, nms, linha)
        if tipo_parametro1 == argumentos[0]:
            verifica_parametros(parametros[1], argumentos[1:], sa, nms, linha)
        else:
            print('Erro semântico no statement %d. Algum dos parâmetros que foram passados para a chamada da função não batem com o tipo correto.' % linha)
            exit()

def conta_parametros(parametros):
    if parametros == None:
        return 0
    else:
        return 1 + conta_parametros(parametros[1])