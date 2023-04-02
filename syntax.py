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
    '''printar : IMPRIMA LPAREN expression RPAREN'''
    print(p[3])

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
    '''expression : operacao'''
    operacao = p[1]
    resto_operacao = p[2]
    if resto_operacao is not None:
        print('aqui')
        if resto_operacao[0] == '+':
            p[0] = operacao + resto_operacao[1]
        elif resto_operacao[0] == '-':
            p[0] = operacao - resto_operacao[1]
        elif resto_operacao[0] == '*':
            p[0] = operacao * resto_operacao[1]
        elif resto_operacao[0] == '/':
            p[0] = operacao / resto_operacao[1] 
    else:
        print('aqui')
        p[0] = operacao



def p_operacao(p):
    '''operacao : NUMERO MAIS NUMERO
    | NUMERO MENOS NUMERO
    | NUMERO VEZES NUMERO
    | NUMERO DIVIDE NUMERO'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_resto_operacao(p):
    '''resto_operacao : MAIS expression
    | MENOS expression
    | VEZES expression
    | DIVIDE expression
    | empty'''
    try:
        p[0] = (p[1], p[2])
    except:
        p[0] = None

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
    print(p)

Parser = yacc.yacc()

