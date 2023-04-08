def p_se(p):
    '''se : SE comparacao LCHAV outro_statement RCHAV senao'''
    p[0] = ('se', p[2], p[4], p[6])

def p_senao(p):
    '''senao : SENAO LCHAV outro_statement RCHAV'''
    p[0] = p[3]

def p_senao_vazio(p):
    '''senao : empty'''
    p[0] = p[1]