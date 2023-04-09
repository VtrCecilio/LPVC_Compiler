from analise_lexica.lexer import Lexer
from analise_sintatica.syntax import Parser
#from analise_semantica.semantic import semantic_analyser as sa
import sys

lex = Lexer()
lex.build()

if len(sys.argv) >= 2:
    with open(sys.argv[1], 'r') as f:
        #lex.test((f.read()))
        result = Parser.parse(f.read())
        #sa(result)

else:
    print("Forneça um arquivo para compilação.")