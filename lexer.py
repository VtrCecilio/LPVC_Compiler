import ply.lex as lex

class Lexer(object):        
    reserved = {
        'se' : 'SE',
        'senao' : 'SENAO',
        'numero' : 'VAR_NUMERO',
        'texto' : 'VAR_TEXTO',
        'imprima' : 'IMPRIMA',
        'leia' : 'LEIA',
        'booleano' : 'VAR_BOOLEANO',
        'verdadeiro' : 'VERDADEIRO',
        'falso' : 'FALSO'
    }
    
    # List of token names.   This is always required
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

    # Regular expression rules for simple tokens
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

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NUMERO(self,t):
        r'\d+(\.\d+)?'
        t.value = float(t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_TEXTO(self,t):
        r'("[^"]*")|(\'[^\']*\')'
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    def t_COMMENT(self,t):
        r'\#.*'
        pass
        # No return value. Token discarded

    # Error handling rule
    def t_error(self,t):
        print("Erro léxico na linha %d! O token '%s' é ilegal. Encerrando compilação." % (t.lineno, t.value[0]))
        exit()

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)
