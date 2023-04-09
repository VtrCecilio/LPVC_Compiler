def p_condicional_laco(p):
    '''condicao_laco : variavel 
    | literal_booleano
    | comparacao'''
    p[0] = p[1]

def p_laco(p):
    '''laco : enquanto'''
    p[0] = p[1]

def p_enquanto(p):
    '''enquanto : ENQUANTO condicao_laco LCHAV outro_statement RCHAV'''
    p[0] = ('enquanto', (p[2], p[4]), p.lineno)
