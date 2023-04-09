import ply.yacc as yacc
from analise_lexica.lexer import Lexer

from analise_sintatica.condicional import *
from analise_sintatica.expressoes import *
from analise_sintatica.funcoes import *
from analise_sintatica.lacos import *
from analise_sintatica.literais import *
from analise_sintatica.declaracao import *

l = Lexer()
tokens = l.get_tokens()

start = 'root'

def p_root(p):
    '''root : statements
    | empty'''
    p[0] = ('root', p[1])

def p_empty(p):
    '''empty :'''
    pass

def p_statements(p):
    '''statements : statement PONTO_VIRGULA outro_statement'''
    p[0] = ('statements', p[1], p[3])

def p_outro_statement(p):
    '''outro_statement : statements
    | empty'''
    p[0] = p[1]

def p_statement(p):
    '''statement : expressao
    | funcao
    | condicional
    | laco
    | declaracao
    | reatribuicao'''
    p[0] = p[1]

def p_error(p):
    try:
        print('Erro sintático na linha %d. Encerrando compilação!' % p.lineno)       
    except:
        print("Erro sintático (faltou um 'ponto e virgula'?). Encerrando compilação!",) 
    exit()

Parser = yacc.yacc()

