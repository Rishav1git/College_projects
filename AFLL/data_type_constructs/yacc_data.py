import ply.yacc as yacc

def p_data_type_declaration(p):
    '''
    data_type_declaration : DATATYPE ID SEMICOLON
    '''
    print(f"Variable {p[2]} declared as {p[1]}")
    pass

def p_empty(p):
    'empty :'
    pass    

def p_error(p):
    print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")