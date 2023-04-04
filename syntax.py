import ply.yacc as yacc
from lexer import Lexer

l = Lexer()
tokens = l.get_tokens()

def p_root(p):
    '''root : statements
    | empty'''
    p[0] = ('root', p[1])

def p_statements(p):
    '''statements : statement PONTO_VIRGULA outro_statement'''
    p[0] = ('statements', p[1], p[3])

def p_outro_statement(p):
    '''outro_statement : statements
    | empty'''
    p[0] = p[1]

def p_statement(p):
    '''statement : imprimir
    | expressao
    | se'''
    p[0] = p[1]
    pass

def p_imprimir(p):
    '''imprimir : IMPRIMA LPAREN algo_imprimir RPAREN'''
    p[0] = ('imprima', p[3])

def p_algo_imprimir(p):
    '''algo_imprimir : expressao'''
    p[0] = p[1]

def p_expressao(p):
    '''expressao : operacao
    | condicional 
    | literal'''
    p[0] = p[1]

def p_condicional(p):
    '''condicional : empty'''
    pass

def p_operacao(p):
    '''operacao : expressao operador expressao resto_operacao'''
    p[0] = ('operacao', p[1], p[2], p[3], p[4])

def p_operacao_paren(p):
    '''operacao : LPAREN expressao RPAREN resto_operacao'''
    p[0] = ('operacao_paren', p[2], p[4])

def p_resto_operacao(p):
    '''resto_operacao : operador expressao resto_operacao'''
    p[0] = ('resto_operacao', p[1], p[2], p[3])

def p_resto_operacao_nula(p):
    '''resto_operacao : empty'''
    p[0] = None

def p_operador(p):
    '''operador : MAIS
    | MENOS
    | VEZES
    | DIVIDE'''
    p[0] = p[1]

def p_literal_numero(p):
    '''literal : NUMERO'''
    p[0] = ('numero', p[1])

def p_literal_texto(p):
    '''literal : TEXTO'''
    p[0] = ('texto', p[1])

def p_literal_booleano(p):
    '''literal : VERDADEIRO
    | FALSO'''
    p[0] = ('booleano', p[1])

def p_se(p):
    '''se : SE condicional LCHAV statements RCHAV senao'''
    p[0] = ('se', p[2], p[4], p[6])

def p_senao(p):
    '''senao : SENAO LCHAV statements RCHAV'''
    p[0] = p[3]

def p_senao_nulo(p):
    '''senao : empty'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print('Erro sintático na linha ' + str(p.lineno) + '. Encerrando compilação!')
    exit()

Parser = yacc.yacc()

