import ply.lex as lex
 
# Daftar token
tokens = (
    'ID', 'NUMBER', 'ASSIGN', 'GT', 'IF', 'ELSE', 'CAT', 'STRING', 'LPAREN', 'RPAREN', 'LCURLY', 'RCURLY', 'SEMICOLON', 'COMMA'
)
 
# Definisi token
t_ASSIGN = r'<-'
t_GT = r'>'
t_STRING = r'\"([^"\\]|(\\.)|(\n))*\"'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_NUMBER = r'\d+'
 
# Fungsi untuk mengenali ID dan kata kunci
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'if':
        t.type = 'IF'  
    elif t.value == 'else':
        t.type = 'ELSE'  
    elif t.value == 'cat':
        t.type = 'CAT'  
    return t
 
# Abaikan spasi dan komentar
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'
 
# Menangani baris baru
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# Menangani karakter ilegal
def t_error(t):
    print(f"Karakter ilegal '{t.value[0]}' di baris {t.lineno}")
    t.lexer.skip(1)
 
# Membangun lexer
lexer = lex.lex()
 
# Contoh input
data = '''num1 <- 10
num2 <- 20
if (num1 > num2) {
    bignum <- num1;
    cat("Big Number is ", bignum, "\n")
} else {
    bignum <- num2;
    cat("Big Number is ", bignum, "\n")
}
'''
 
# Proses tokenisasi
lexer.input(data)
print("Hasil Tokenisasi:")
for tok in lexer:
    print(tok)