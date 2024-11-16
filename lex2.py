import ply.lex as lex

# Daftar token
tokens = (
    'ID', 'NUMBER', 'ASSIGN', 'PLUS', 'DIVIDE', 'LPAREN', 'RPAREN', 'CAT', 'STRING', 'SEMICOLON', 'COMMA'
)

# Definisi token
t_ASSIGN = r'<-'
t_PLUS = r'\+'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'\"([^"\\\n]|(\\.)|(\n))*\"'
t_SEMICOLON = r';'
t_COMMA = r','
t_NUMBER = r'\d+'

# Fungsi untuk mengenali ID dan kata kunci
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'cat':
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
data = '''num1 <- 10
num2 <- 20
num3 <- 30
sum <- num1 + num2 + num3
avg <- sum / 3
cat("num1 is ", num1, "\n")
cat("num2 is ", num2, "\n")
cat("num3 is ", num3, "\n")
cat("Sum 3 numbers is ", sum, "\n")
cat("Average is ", avg, "\n")
'''

# Tokenizing
lexer.input(data)
for tok in lexer:
    print(tok)