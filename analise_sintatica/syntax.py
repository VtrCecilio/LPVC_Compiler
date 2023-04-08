import ply.yacc as yacc
from analise_lexica.lexer import Lexer

from analise_sintatica.condicional import *
from analise_sintatica.expressoes import *
from analise_sintatica.funcoes import *
from analise_sintatica.lacos import *
from analise_sintatica.literais import *
from analise_sintatica.tipos import *

l = Lexer()
tokens = l.get_tokens()

def p_root(p):
    '''root : statements
    | empty'''
    p[0] = ('root', p[1])

def p_empty(p):
    '''empty :'''
    pass

def p_variavel(p):
    '''variavel : ID'''
    p[0] = ('variavel', p[1])

def p_statements(p):
    '''statements : statement PONTO_VIRGULA outro_statement'''
    p[0] = ('statements', p[1], p[3])

def p_outro_statement(p):
    '''outro_statement : statements
    | empty'''
    p[0] = p[1]

def p_statement(p):
    '''statement : imprimir
    | ler
    | expressao
    | se
    | enquanto'''
    p[0] = p[1]


# def p_declaracao(p):
#     '''declaracao : VAR_NUMERO ID atribuicao_numero
#     | VAR_TEXTO ID atribuicao_texto
#     | VAR_BOOLEANO ID atribuicao_booleano'''
#     p[0] = ('declaracao', p[2], p[3])

# def p_atribuicao_numero(p):
#     '''atribuicao_numero : RECEBE operacao'''
#     p[0] = ('atribuicao_numero', p[2])

# def p_atribuicao_numero_vazio(p):
#     '''atribuicao_numero : empty'''
#     p[0] = ('atribuicao_numero', ('numero_vazio', None))

# def p_atribuicao_texto(p):
#     '''atribuicao_texto : RECEBE texto'''
#     p[0] = ('atribuicao_texto', p[2])

# def p_atribuicao_texto_vazio(p):
#     '''atribuicao_texto : empty'''
#     p[0] = ('atribuicao_texto', ('texto_vazio', None))

# def p_atribuicao_booleano(p):
#     '''atribuicao_booleano : RECEBE booleano'''
#     p[0] = ('atribuicao_booleano', p[2])

# def p_atribuicao_booleano_vazio(p):
#     '''atribuicao_booleano : empty'''
#     p[0] = ('atribuicao_booleano', ('booleano_vazio', None))
    
# def p_reatribuicao(p):
#     'reatribuicao : ID RECEBE resto_reatribuicao'
#     p[0] = ('reatribuicao', p[1], p[3])

# def p_resto_reatribuicao(p):
#     '''resto_reatribuicao : ID
#     | operacao
#     | texto
#     | booleano'''
#     p[0] = p[1]

def p_error(p):
    try:
        print(p)
        print('Erro sintático na linha %d. Encerrando compilação!' % p.lineno)       
    except:
        print('Erro sintático, linha não detectada. Encerrando compilação!',) 
    exit()

Parser = yacc.yacc()

