import ply.lex as lex
import ply.yacc as yacc
from lex_data import *
from yacc_data import *

lexer = lex.lex()
parser = yacc.yacc()

# input_text = """
# int age;
# float price;
# bool isAvailable;
# string name;
# """

input_text = input("enter any loop in C# to see syntax validation data type declaration (write syntax in one line) : ")
result = parser.parse(input_text)