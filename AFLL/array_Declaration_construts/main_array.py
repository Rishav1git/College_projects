import ply.lex as lex
import ply.yacc as yacc
from lex_array import *
from yacc_array import *

lexer = lex.lex()
parser = yacc.yacc()

# input_text = "int[] numbers"
input_text = input("enter any loop in C# to see syntax validation array declaration (write syntax in one line) : ")
parser.parse(input_text, lexer=lexer)