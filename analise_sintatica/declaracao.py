def p_tipo_variavel(p):
    '''tipo_variavel : VAR_NUMERO
    | VAR_TEXTO
    | VAR_BOOLEANO'''
    p[0] = p[1]

# Declarações para variáveis
def p_declaracao(p):
    '''declaracao : tipo_variavel ID RECEBE expressao'''
    p[0] = ('declaracao', p[1], p[2], p[4])

def p_reatribuicao(p):
    'reatribuicao : ID RECEBE expressao'
    p[0] = ('reatribuicao', p[1], p[3])


# Declaração para funções
def p_declara_funcao(p):
    '''declaracao : PROCEDIMENTO ID LPAREN argumentos RPAREN LCHAV outro_statement RCHAV'''
    p[0] = ('procedimento', p[2], p[4], p[7])

def p_argumentos_nulo(p):
    '''argumentos : empty'''
    pass

def p_argumentos(p):
    '''argumentos : tipo_variavel ID resto_argumentos'''
    p[0] = (p[1], p[2])

def p_resto_argumentos_nulo(p):
    '''resto_argumentos : empty'''
    pass

def p_resto_argumentos(p):
    '''resto_argumentos : VIRGULA argumentos'''
    p[0] = p[2]
