import ply.lex as lex
import ply.yacc as yacc
from lex_operator import *
from yacc_operator import *

lexer = lex.lex()
parser = yacc.yacc()

# input_code = "2 + 3 * 4"
input_code = input("enter any loop in C# to see syntax validation operator validation (write syntax in one line) : ")
result = parser.parse(input_code)
print(f"Result: {result}")



