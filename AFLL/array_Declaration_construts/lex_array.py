import ply.lex as lex

tokens = (
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'DATATYPE',
    'ID',
)

t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_ignore = ' \t'
t_DATATYPE = r'int|float|double|char|bool'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

