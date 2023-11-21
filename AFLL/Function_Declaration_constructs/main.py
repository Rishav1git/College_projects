import ply.lex as lex
import ply.yacc as yacc
from lex_function import *
from yacc_function import *

lexer = lex.lex()
parser = yacc.yacc()

# input_text = """
# protected void PrintMessage();
# public int Add();
# private double CalculateTax();
# """

input_text = input("enter any loop in C# to see syntax validation data type declaration (write syntax in one line) : ")
result = parser.parse(input_text)