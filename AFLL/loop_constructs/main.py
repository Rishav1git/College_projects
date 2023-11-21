import ply.lex as lex
import ply.yacc as yacc
from lex_loop import *
from yacc_loop import *

lexer = lex.lex()
parser = yacc.yacc()

# input_text = '''
# for (int i = 0; i < 5; i++) {
#     printf(" %d", i);
# }

# while (int j < 10) { printf(" loop: %d", j); j++; }

# do {
#     int k;
#     printf("loop: %d", k);
#     k++;
# } while (k < 3);
# '''
input_text = input("enter any loop in C# to see syntax validation for loops (write syntax in one line) : ")
result = parser.parse(input_text)

