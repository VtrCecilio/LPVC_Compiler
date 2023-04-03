import ply.yacc as yacc
from lexer import Lexer

l = Lexer()
tokens = l.get_tokens()

def p_program(p):
    '''program : statement resto_statement
    | empty'''
    pass

def p_statement(p):
    '''statement : expression
    | atribuicao
    | forma_condicional
    | printar'''
    pass

def p_resto_statements(p):
    '''resto_statement : PONTO_VIRGULA
    | PONTO_VIRGULA statement resto_statement'''
    pass


def p_printar(p):
    '''printar : printarpl
    | printarsempl'''
    pass

def p_printar_com_pl(p):
    '''printarpl : IMPRIMAPL LPAREN expression RPAREN'''
    print(p[3])


def p_printar_sem_pl(p):
    '''printarsempl : IMPRIMA LPAREN expression RPAREN'''
    print(p[3], end='')

def p_forma_condicional(p):
    '''forma_condicional : SE LPAREN condicional RPAREN LCHAV statement RCHAV resto_condicional'''
    pass

def p_resto_condicional(p):
    '''resto_condicional : SENAO LCHAV statement RCHAV
    | empty'''
    pass

def p_condicional(p):
    '''condicional : expression MAIORIGUAL expression
    | expression MENORIGUAL expression
    | expression IGUAL expression
    | expression MAIOR expression
    | expression MENOR expression
    | expression DIFER expression'''
    pass

def p_expression(p):
    '''expression : numero
    | empty'''
    if p[1] != None: 
        p[0] = p[1]

def p_numero_sem_paren(p):
    '''numero : NUMERO operacao'''
    if p[2] == None:
        p[0] = p[1]
    else:
        operacao = p[2]
        if operacao[0] == '+':
            p[0] = p[1] + operacao[1]
        elif operacao[0] == '-':
            p[0] = p[1] - operacao[1]
        elif operacao[0] == '*':
            p[0] = p[1] * operacao[1]
        elif operacao[0] == '/':
            p[0] = p[1] / operacao[1]

def p_numero_com_paren(p):
    '''numero : LPAREN NUMERO operacao RPAREN operacao'''
    if p[3] == None:
        p[0] = p[2]
    else:
        operacao = p[3]
        if operacao[0] == '+':
            p[0] = p[2] + operacao[1]
        elif operacao[0] == '-':
            p[0] = p[2] - operacao[1]
        elif operacao[0] == '*':
            p[0] = p[2] * operacao[1]
        elif operacao[0] == '/':
            p[0] = p[2] / operacao[1]

    if p[5] != None:
        operacao = p[5]
        if operacao[0] == '+':
            p[0] = p[0] + operacao[1]
        elif operacao[0] == '-':
            p[0] = p[0] - operacao[1]
        elif operacao[0] == '*':
            p[0] = p[0] * operacao[1]
        elif operacao[0] == '/':
            p[0] = p[0] / operacao[1]

def p_operacao(p):
    '''operacao : MAIS expression
    | MENOS expression
    | VEZES expression
    | DIVIDE expression
    | empty'''
    if p[1] == None:
        p[0] = None
    else:
        p[0] = (p[1], p[2])

def p_atribuicao(p):
    '''atribuicao : VAR_NUMERO ID RECEBE expression
    | VAR_TEXTO ID RECEBE TEXTO'''
    pass

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

Parser = yacc.yacc()

