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
    | ler
    | expressao
    | se
    | enquanto
    | declaracao
    | reatribuicao'''
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
    | literal
    | variavel'''
    p[0] = p[1]

def p_variavel(p):
    '''variavel : ID'''
    p[0] = ('variavel', p[1])

def p_ler(p):
    '''ler : LEIA LPAREN variavel RPAREN'''
    p[0] = ('leia', p[3])

def p_condicao(p):
    '''condicao : operacao condicional operacao'''
    p[0] = ('condicao', p[1], p[2], p[3])

def p_condicao_paren(p):
    '''condicao : LPAREN operacao condicional operacao RPAREN'''
    p[0] = ('condicao', p[2], p[3], p[4])

def p_condicao_unica(p):
    '''condicao : literal_booleano
    | variavel'''
    p[0] = ('condicao_unica', p[1])

def p_condicao_literal_paren(p):
    '''condicao : LPAREN literal_booleano RPAREN'''
    p[0] = p[2]

def p_condicional(p):
    '''condicional : MAIORIGUAL
    | MENORIGUAL
    | IGUAL
    | MAIOR
    | MENOR
    | DIFER'''
    p[0] = p[1]

def p_operacao(p):
    '''operacao : operando operador operacao resto_operacao'''
    p[0] = ('operacao_full', p[1], p[2], p[3], p[4])

def p_operacao_paren(p):
    '''operacao : LPAREN operacao RPAREN resto_operacao'''
    p[0] = ('operacao_paren', p[2], p[4])

def p_operacao_literal(p):
    '''operacao : operando'''
    p[0] = ('operacao_operando_unico', p[1])

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

def p_operando(p):
    '''operando : variavel
    | literal_numero'''
    p[0] = p[1]

def p_booleano(p):
    '''booleano : condicao'''
    p[0] = p[1]

def p_texto(p):
    '''texto : variavel
    | literal_texto'''
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

def p_declaracao(p):
    '''declaracao : VAR_NUMERO ID atribuicao_numero
    | VAR_TEXTO ID atribuicao_texto
    | VAR_BOOLEANO ID atribuicao_booleano'''
    p[0] = ('declaracao', p[2], p[3])

def p_atribuicao_numero(p):
    '''atribuicao_numero : RECEBE operacao'''
    p[0] = ('atribuicao_numero', p[2])

def p_atribuicao_numero_vazio(p):
    '''atribuicao_numero : empty'''
    p[0] = ('atribuicao_numero', ('numero_vazio', None))

def p_atribuicao_texto(p):
    '''atribuicao_texto : RECEBE texto'''
    p[0] = ('atribuicao_texto', p[2])

def p_atribuicao_texto_vazio(p):
    '''atribuicao_texto : empty'''
    p[0] = ('atribuicao_texto', ('texto_vazio', None))

def p_atribuicao_booleano(p):
    '''atribuicao_booleano : RECEBE booleano'''
    p[0] = ('atribuicao_booleano', p[2])

def p_atribuicao_booleano_vazio(p):
    '''atribuicao_booleano : empty'''
    p[0] = ('atribuicao_booleano', ('booleano_vazio', None))
    
def p_reatribuicao(p):
    'reatribuicao : ID RECEBE resto_reatribuicao'
    p[0] = ('reatribuicao', p[1], p[3])

def p_resto_reatribuicao(p):
    '''resto_reatribuicao : ID
    | operacao
    | texto
    | booleano'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    try:
        print(p)
        print('Erro sintático na linha %d. Encerrando compilação!' % p.lineno)       
    except:
        print('Erro sintático, linha não detectada. Encerrando compilação!',) 
    exit()

Parser = yacc.yacc()

