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
    | se
    | enquanto'''
    p[0] = p[1]

def p_imprimir(p):
    '''imprimir : IMPRIMA LPAREN algo_imprimir RPAREN'''
    p[0] = ('imprima', p[3])

def p_algo_imprimir(p):
    '''algo_imprimir : expressao'''
    p[0] = p[1]

def p_expressao(p):
    '''expressao : operacao
    | condicao
    | literal'''
    p[0] = p[1]

def p_condicao(p):
    '''condicao : expressao condicional expressao'''
    p[0] = ('condicao', p[1], p[2], p[3])

def p_condicao_paren(p):
    '''condicao : LPAREN expressao condicional expressao RPAREN'''
    p[0] = ('condicao', p[2], p[3], p[4])

def p_condicional(p):
    '''condicional : MAIORIGUAL
    | MENORIGUAL
    | IGUAL
    | MAIOR
    | MENOR
    | DIFER'''
    p[0] = p[1]

def p_operacao(p):
    '''operacao : NUMERO operador NUMERO resto_operacao'''
    p[0] = ('operacao_full', p[1], p[2], p[3], p[4])

def p_operacao_paren(p):
    '''operacao : LPAREN operacao RPAREN resto_operacao'''
    p[0] = ('operacao_paren', p[2], p[4])

def p_operacao_literal(p):
    '''operacao : literal_numero'''
    p[0] = ('operacao_literal', p[1])

def p_resto_operacao(p):
    '''resto_operacao : operador operacao'''
    p[0] = ('resto_operacao', p[1], p[2])

def p_resto_operacao_nula(p):
    '''resto_operacao : empty'''
    p[0] = None

def p_operador(p):
    '''operador : MAIS
    | MENOS
    | VEZES
    | DIVIDE'''
    p[0] = p[1]

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

def p_se(p):
    '''se : SE condicao LCHAV outro_statement RCHAV senao'''
    p[0] = ('se', p[2], p[4], p[6])

def p_senao(p):
    '''senao : SENAO LCHAV outro_statement RCHAV'''
    p[0] = p[3]

def p_senao_nulo(p):
    '''senao : empty'''
    p[0] = p[1]

def p_enquanto(p):
    '''enquanto : ENQUANTO condicao LCHAV outro_statement RCHAV'''
    p[0] = ('enquanto', p[2], p[4])

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    try:
        print('Erro sintático na linha %d. Encerrando compilação!' % p.lineno)       
    except:
        print('Erro sintático, linha não detectada. Encerrando compilação!',) 
    exit()

Parser = yacc.yacc()

