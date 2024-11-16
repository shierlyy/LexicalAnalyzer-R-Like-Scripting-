import ply.lex as lex

# Daftar token
tokens = (
    'PRINT', 'CAT', 'STRING', 'LPAREN', 'RPAREN', 'SEMICOLON'
)

# Definisi token
t_PRINT = r'print'
t_CAT = r'cat'
t_STRING = r'\".*?\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'

# Ignore whitespace and newline
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

# Handling newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Contoh input
data = '''print("Hello, world!");
cat("Thanks")
'''

# Tokenizing
lexer.input(data)
for tok in lexer:
    print(tok)