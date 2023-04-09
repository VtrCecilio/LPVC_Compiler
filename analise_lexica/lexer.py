import ply.lex as lex

class Lexer(object):        
    # Palavras reservadas da linguagem. São "unidas" aos tokens
    reserved = {
        'se' : 'SE',
        'enquanto' : 'ENQUANTO',
        'senao' : 'SENAO',
        'numero' : 'VAR_NUMERO',
        'texto' : 'VAR_TEXTO',
        'imprima' : 'IMPRIMA',
        'leia' : 'LEIA',
        'booleano' : 'VAR_BOOLEANO',
        'verdadeiro' : 'VERDADEIRO',
        'falso' : 'FALSO'
    }
    
    # Tipos de Tokens que existem na linguagem
    tokens = [
       'NUMERO',
       'TEXTO',
       'MAIS',
       'MENOS',
       'VEZES',
       'DIVIDE',
       'LPAREN',
       'RPAREN',
       'LCHAV',
       'RCHAV',
       'ID',
       'MAIORIGUAL',
       'MAIOR',
       'MENORIGUAL',
       'MENOR',
       'IGUAL',
       'RECEBE',
       'DIFER',
       'PONTO_VIRGULA',
     ] + list(reserved.values())

    def get_tokens(self):
        return self.tokens

    # Expressões regulares para Tokens simples
    t_MAIORIGUAL = r'\>\='
    t_MAIOR = r'\>'
    t_MENORIGUAL = r'\<\='
    t_MENOR = r'\<'
    t_IGUAL = r'\=\='
    t_RECEBE = r'\='
    t_DIFER = r'\<\>'
    t_MAIS    = r'\+'
    t_MENOS   = r'\-'
    t_VEZES   = r'\*'
    t_DIVIDE  = r'\/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_LCHAV  = r'\{'
    t_RCHAV  = r'\}'
    t_PONTO_VIRGULA = r'\;'


    # Regular Expression para literais do tipo 'numero'
    def t_NUMERO(self,t):
        r'\d+(\.\d+)?'
        t.value = float(t.value)
        return t

    # Seta um tracker para número de linhas
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    # Regular Expression para literais do tipo 'texto'
    def t_TEXTO(self,t):
        r'("[^"]*")|(\'[^\']*\')'
        return t

    # Reconheço tokens do tipo 'ID', se for palavra reservada, o converte para tipo correto.
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')
        return t

    # Ignora spaços e tabs
    t_ignore  = ' \t'

    # Ignora linhas comentários, começam com '#'
    def t_COMMENT(self,t):
        r'\#.*'
        pass

    # Mensagem default para erros léxicos
    def t_error(self,t):
        print("Erro léxico na linha %d! O token '%s' é ilegal. Encerrando compilação." % (t.lineno, t.value[0]))
        exit()

    # Builder do Lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Método para testar o Lexer
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)
