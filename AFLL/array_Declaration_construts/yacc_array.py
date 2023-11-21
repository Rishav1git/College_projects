import ply.yacc as yacc

def p_array_declaration(p):
    '''
    array_declaration : DATATYPE LBRACKET  RBRACKET ID
                     | DATATYPE LBRACKET  RBRACKET array_declaration
    '''
    print("Found array")
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Syntax error")
