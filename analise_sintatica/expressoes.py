# Expressões, base
def p_expressao(p):
    '''expressao : literal
    | comparacao
    | operacao
    | variavel
    | chama_procedimento'''
    p[0] = p[1]

def p_variavel(p):
    '''variavel : ID'''
    p[0] = ('variavel', p[1])

# Expressões, parte operações matematicas
def p_operador(p):
    '''operador : MAIS
    | MENOS
    | VEZES
    | DIVIDE'''
    p[0] = p[1]

def p_operacao(p):
    '''operacao : expressao operador expressao resto_operacao'''
    p[0] = ('operacao_binaria', p[1], p[2], p[3], p[4])

def p_operacao_parenteses(p):
    '''operacao : LPAREN expressao RPAREN resto_operacao'''
    p[0] = ('operacao_parenteses', p[2], p[4])

def p_resto_operacao(p):
    '''resto_operacao : operador expressao'''
    p[0] = ('resto_operacao', p[1], p[2])

def p_resto_operacao_nula(p):
    '''resto_operacao : empty'''
    pass

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
    '''comparacao : expressao comparador expressao'''
    p[0] = ('comparacao', p[1], p[2], p[3])

def p_condicao_paren(p):
    '''comparacao : LPAREN expressao comparador expressao RPAREN'''
    p[0] = ('comparacao', p[2], p[3], p[4])


# Expressões, chama um procedimento
def p_chama_procedimento(p):
    '''chama_procedimento : ID LPAREN parametros RPAREN'''
    p[0] = ('chama_procedimento', p[1], p[3])


def p_parametro_nulo(p):
    '''parametros : empty'''
    pass

def p_parametros(p):
    '''parametros : expressao resto_parametros'''
    p[0] = (p[1], p[2])

def p_resto_parametros_nulo(p):
    '''resto_parametros : empty'''
    pass

def p_resto_parametros(p):
    '''resto_parametros : VIRGULA parametros'''
    p[0] = p[2]