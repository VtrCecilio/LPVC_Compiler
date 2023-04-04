from lexer import Lexer
from syntax import Parser
from semantic import semantic_analyser as sa
import sys


lex = Lexer()
lex.build()

if len(sys.argv) >= 2:
    with open(sys.argv[1], 'r') as f:
        #lex.test((f.read()))
        result = Parser.parse(f.read())
        sa(result)

else:
    print("Forneça um arquivo para compilação.")