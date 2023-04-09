def p_literal(p):
    '''literal : literal_numero
    | literal_texto
    | literal_booleano'''
    p[0] = p[1]

def p_literal_numero(p):
    '''literal_numero : NUMERO'''
    p[0] = ('numero', p[1])

def p_literal_texto(p):
    '''literal_texto : TEXTO'''
    p[0] = ('texto', p[1])

def p_literal_booleano(p):
    '''literal_booleano : VERDADEIRO
    | FALSO'''
    p[0] = ('booleano', p[1])