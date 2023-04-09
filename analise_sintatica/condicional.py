def p_condicao_se(p):
    '''condicao_se : comparacao
    | literal_booleano
    | variavel'''
    p[0] = p[1]

def p_se(p):
    '''condicional : SE condicao_se LCHAV outro_statement RCHAV senao'''
    p[0] = ('se', p[2], p[4], p[6])

def p_senao(p):
    '''senao : SENAO LCHAV outro_statement RCHAV'''
    p[0] = p[3]

def p_senao_vazio(p):
    '''senao : empty'''
    pass