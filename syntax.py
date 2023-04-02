import ply.yacc as yacc

from lexer import Lexer

l = Lexer()
tokens = l.get_tokens()

def p_program(p):
    '''program : statement
    | empty'''
    pass

def p_statement(p):
    '''statement : expression resto_statement
    | atribuicao resto_statement
    | forma_condicional resto_statement
    | IMPRIMA LPAREN expression RPAREN resto_statement'''
    pass

def p_resto_statements(p):
    '''resto_statement : PONTO_VIRGULA
    | PONTO_VIRGULA statement'''
    pass

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
    '''expression : operacao
    | NUMERO
    | TEXTO'''
    pass

def p_operacao(p):
    '''operacao : NUMERO MAIS NUMERO
    | NUMERO MENOS NUMERO
    | NUMERO VEZES NUMERO
    | NUMERO DIVIDE NUMERO'''
    pass

def p_atribuicao(p):
    '''atribuicao : VAR ID RECEBE resto_atribuicao'''
    pass

def p_resto_atribuicao(p):
    '''resto_atribuicao : expression
    | condicional'''
    pass

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)

Parser = yacc.yacc()

