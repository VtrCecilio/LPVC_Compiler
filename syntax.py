import ply.yacc as yacc
from lexer import Lexer

l = Lexer()
tokens = l.get_tokens()

namespace = dict()

def p_program(p):
    '''program : statement resto_statement
    | empty'''
    pass

def p_statement(p):
    '''statement : expression
    | atribuicao
    | reatribuicao
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
    | TEXTO
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

def p_numero_var(p):
    '''numero : ID operacao'''
    try:
        variavel = namespace[p[1]]
        p[0] = variavel[1]

        if p[2] != None:
            operacao = p[2]
            if operacao[0] == '+':
                p[0] = p[0] + operacao[1]
            elif operacao[0] == '-':
                p[0] = p[0] - operacao[1]
            elif operacao[0] == '*':
                p[0] = p[0] * operacao[1]
            elif operacao[0] == '/':
                p[0] = p[0] / operacao[1]
    except:
        print('Erro: Variavel não declarada')

def p_numero_com_paren(p):
    '''numero : LPAREN numero RPAREN operacao'''
    p[0] = p[2]

    if p[4] != None:
        operacao = p[4]
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
    if type(p[4]) is str:
        namespace[p[2]] = [p[1], p[4]]
    elif p[4] != None:
        namespace[p[2]] = [p[1], p[4]]
    else:
        print('erro')

def p_reatribuicao(p):
    '''reatribuicao : ID RECEBE valor'''
    try:
        variavel = namespace[p[1]]
        valor = p[3]
        if variavel[0] == valor[0]:
            variavel[1] = valor[1]
        else:
            print('erro: tipos diferentes') 
    except:
        print('erro: varivel não declarada')

def p_reatribuicao_tipo(p):
    '''valor : expression'''
    if type(p[1]) is float:
        p[0] = ['numero', p[1]]
    elif type(p[1]) is str:
        p[0] = ['texto', p[1]]
    else:
        pass

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)

Parser = yacc.yacc()

