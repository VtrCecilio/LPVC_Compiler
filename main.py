from lexer import Lexer
from syntax import Parser
import sys


lex = Lexer()
lex.build()
parser = Parser

if len(sys.argv) >= 2:
    with open(sys.argv[1], 'r') as f:
        #lex.test((f.read()))

        result = parser.parse(f.read())
    
else:
    print("Forneça um arquivo para compilação.")