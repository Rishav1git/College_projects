import ply.yacc as yacc

precedence = ()

def p_program(p):
    '''program : program statement
               | empty'''
    pass

def p_statement(p):
    '''statement : for_loop
                 | while_loop
                 | do_while_loop
                 | INT
                 | LESS_THAN
                 | OPEN_PAREN
                 | CLOSE_PAREN
                 | OPEN_BRACE
                 | CLOSE_BRACE
                 | SEMICOLON
                 '''
    pass

def p_for_loop(p):
    '''for_loop : FOR OPEN_PAREN DATATYPE ID EQUAL INT SEMICOLON ID LESS_THAN INT SEMICOLON ID PLUS PLUS CLOSE_PAREN OPEN_BRACE PRINTF OPEN_PAREN STRING  COMMA ID CLOSE_PAREN SEMICOLON CLOSE_BRACE'''
    print("Found a for loop")


def p_while_loop(p):
    '''while_loop : WHILE OPEN_PAREN DATATYPE ID LESS_THAN INT CLOSE_PAREN OPEN_BRACE PRINTF OPEN_PAREN STRING COMMA ID CLOSE_PAREN SEMICOLON ID PLUS PLUS SEMICOLON CLOSE_BRACE'''
    print("Found a while loop")

def p_do_while_loop(p):
    '''do_while_loop : DO OPEN_BRACE DATATYPE ID SEMICOLON PRINTF OPEN_PAREN STRING COMMA ID CLOSE_PAREN SEMICOLON ID PLUS PLUS SEMICOLON CLOSE_BRACE WHILE OPEN_PAREN ID LESS_THAN INT CLOSE_PAREN SEMICOLON'''
    print("Found a do-while loop")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")
