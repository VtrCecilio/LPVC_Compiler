import ply.yacc as yacc
from lexer import Lexer

l = Lexer()
tokens = l.get_tokens()

class Node:
    def __init__(self,type,children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf

def p_program(p):
    '''program : statements
    | empty'''
    p[0] = Node('start_statements', [p[1]])


def p_literal_numero(p):
    '''numero : NUMERO'''
    p[0] = 

def p_literal_texto(p):
    '''texto : TEXTO'''
    p[0] = 

def p_empty(p):
    '''empty :'''

def p_error(p):
    print(p)

Parser = yacc.yacc()

