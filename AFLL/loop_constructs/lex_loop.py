import ply.lex as lex

tokens = (
    'FOR',
    'WHILE',
    'DO',
    'ID',
    'INT',
    'LESS_THAN',
    'OPEN_PAREN',
    'CLOSE_PAREN',
    'OPEN_BRACE',
    'CLOSE_BRACE',
    'SEMICOLON',
    'COMMA',
    'PRINTF',
    'EQUAL',
    'PLUS',
    'STRING',
    'DATATYPE', 
)

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INT = r'\d+'
t_LESS_THAN = r'<'
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'
t_OPEN_BRACE = r'\{'
t_CLOSE_BRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_EQUAL = r'='
t_PLUS = r'\+'
t_ignore = ' \t'

def t_FOR(t):
    r'for'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_DO(t):
    r'do'
    return t
def t_PRINTF(t):
    r'printf'
    return t
def t_STRING(t):
    r'"([^"\\]|\\.)*"'  
    return t
def t_DATATYPE(t):
    r'int|char|float|double|void'
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
    
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)



