# Funções built-in
def p_funcoes(p):
    '''funcao : imprimir 
    | ler'''
    p[0] = p[1]

def p_imprimir(p):
    '''imprimir : IMPRIMA LPAREN entrada_imprimir RPAREN'''
    p[0] = ('imprima', (p[3]), p.lineno)

def p_algo_imprimir(p):
    '''entrada_imprimir : expressao'''
    p[0] = p[1]

def p_ler(p):
    '''ler : LEIA LPAREN variavel RPAREN'''
    p[0] = ('leia', (p[3]), p.lineno)