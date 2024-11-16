import ply.lex as lex

# Daftar token
tokens = (
    'CAT', 'NUMBER', 'ASSIGN', 'MOD', 'NEQ', 'WHILE', 'IF', 'STRING', 'LPAREN', 
    'RPAREN', 'LCURLY', 'RCURLY', 'SEMICOLON', 'COMMA', 'PLUS', 'LTE', 'ID'
)

# Definisi token
t_ASSIGN = r'<-'
t_MOD = r'%'
t_NEQ = r'!='
t_STRING = r'\"([^"\\]|(\\.)|(\n))*\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_PLUS = r'\+'
t_LTE = r'<='
t_NUMBER = r'\d+'

# Fungsi untuk mengenali ID dan kata kunci
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'if':
        t.type = 'IF'
    elif t.value == 'while':
        t.type = 'WHILE'
    elif t.value == 'cat':
        t.type = 'CAT'
    return t

# Ignore whitespace and comments
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
data = '''cat("List of Odd Number 1-100: \n")
num <- 1
while (num <= 100) {
    sisa <- (num % 2)
    if (sisa != 0) {
        oddnum <- num
        cat(oddnum, " ")
    }
    num <- num + 1
}
'''

# Tokenizing
lexer.input(data)
for tok in lexer:
    print(tok)