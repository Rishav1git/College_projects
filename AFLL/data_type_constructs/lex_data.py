import ply.lex as lex

tokens = (
    'DATATYPE',
    'ID',
    'SEMICOLON',
)

def t_DATATYPE(t):
    r'int|float|bool|string'
    return t
t_SEMICOLON = r';'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
