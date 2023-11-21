import ply.yacc as yacc

def p_function_declaration(p):
    '''
    function_declaration :  ACCESS_MODIFIER RETURN_TYPE ID LPAREN RPAREN SEMICOLON
    '''
    # Process the function declaration here
    access_modifier = p[1]
    return_type = p[2]
    function_name = p[3]
    print(f"Function Declaration: {access_modifier} {return_type} {function_name}();")


def p_error(p):
    print(f"Syntax error at line {p.lineno}: Unexpected token '{p.value}'")