# Expressões, base
def p_expressao(p):
    '''expressao : operacao
    | booleano
    | texto'''
    p[0] = p[1]

# Expressões, parte operações matematicas
def p_operando(p):
    '''operando : literal_numero'''
    p[0] = p[1]

def p_operador(p):
    '''operador : MAIS
    | MENOS
    | VEZES
    | DIVIDE'''
    p[0] = p[1]

def p_operacao(p):
    '''operacao : operando operador operacao resto_operacao'''
    p[0] = ('operacao_binaria', p[1], p[2], p[3], p[4])

def p_operacao_parenteses(p):
    '''operacao : LPAREN operacao RPAREN resto_operacao'''
    p[0] = ('operacao_parenteses', p[2], p[4])

def p_operacao_operando(p):
    '''operacao : operando'''
    p[0] = ('operacao_unico', p[1])

def p_resto_operacao(p):
    '''resto_operacao : operador operacao'''
    p[0] = ('resto_operacao', p[1], p[2])

def p_resto_operacao_nula(p):
    '''resto_operacao : empty'''
    p[0] = None


# Expressões, parte comparativa
def p_condicional(p):
    '''comparador : MAIORIGUAL
    | MENORIGUAL
    | IGUAL
    | MAIOR
    | MENOR
    | DIFER'''
    p[0] = p[1]

def p_comparacao(p):
    '''comparacao : operacao comparador operacao'''
    p[0] = ('comparacao', p[1], p[2], p[3])

def p_condicao_paren(p):
    '''comparacao : LPAREN operacao comparador operacao RPAREN'''
    p[0] = ('comparacao', p[2], p[3], p[4])