def p_booleano(p):
    '''booleano : variavel
    | literal_booleano'''
    p[0] = p[1]

def p_texto(p):
    '''texto : variavel
    | literal_texto'''
    p[0] = p[1]