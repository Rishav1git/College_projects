import ply.lex as lex

tokens = (
    'ACCESS_MODIFIER',
    'RETURN_TYPE',
    'ID',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'COMMA',
)

def t_RETURN_TYPE(t):
    r'float|bool|string|double|void|int'
    return t
def t_ACCESS_MODIFIER(t):
    r'(public|private|protected|default)'
    return t
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)