def p_declaracao(p):
    '''declaracao : VAR_NUMERO ID RECEBE expressao
    | VAR_TEXTO ID expressao
    | VAR_BOOLEANO ID expressao'''
    p[0] = ('declaracao', (p[1], p[2], p[4]), p.lineno)

def p_reatribuicao(p):
    'reatribuicao : ID RECEBE expressao'
    p[0] = ('reatribuicao', (p[1], p[3]), p.lineno)

