from etoken import EToken

class EParser:
    def __init__(self, lexer):
        self.lexer = lexer  # ELexer instance
        self.curr_token = None  # Current EToken

    def error(self, msg="Syntax error"):
        print(msg)
        quit(1)  # Stops execution with an error

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == EToken.ERROR:  # Lexical error
            self.error()

    def parse(self):
        self.next_token()
        self.statements()

    def statements(self):
        if self.curr_token.token_code == EToken.END:
            print()  # Print the final blank line
            quit(1)
        else:
            self.statement()
            if self.curr_token.token_code == EToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error()  # Missing semicolon

    def statement(self):
        if self.curr_token.token_code == EToken.ID:
            var_name = self.curr_token.lexeme
            self.next_token()
            if self.curr_token.token_code == EToken.ASSIGN:
                self.next_token()
                self.expr()
                print(f"ASSIGN {var_name}")
            else:
                self.error()  # Missing assignment operator
        elif self.curr_token.token_code == EToken.PRINT:
            self.next_token()
            if self.curr_token.token_code == EToken.ID:
                print(f"PRINT {self.curr_token.lexeme}")
                self.next_token()
            else:
                self.error()  # Print statement syntax error

    def expr(self):
        self.term()
        while self.curr_token.token_code in [EToken.PLUS, EToken.MINUS]:
            op = self.curr_token
            self.next_token() 
        
            if self.curr_token.token_code not in [EToken.INT, EToken.ID, EToken.LPAREN]:
                self.error("Syntax error")
                return
            else:
                self.term()
                if op.token_code == EToken.PLUS:
                    print("ADD")
                elif op.token_code == EToken.MINUS:
                    print("SUB")

    def term(self):
        self.factor()
        while self.curr_token.token_code == EToken.MULT:
            self.next_token()
            self.factor()
            print("MULT")

    def factor(self):
        if self.curr_token.token_code in [EToken.INT, EToken.ID]:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()
        elif self.curr_token.token_code == EToken.LPAREN:
            self.next_token()
            self.expr()
            if self.curr_token.token_code != EToken.RPAREN:
                self.error()
            self.next_token()
        else:
            self.error()



"""import sys
from etoken import EToken

class EParser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token = None

    def parse(self):
        self.next_token()
        self.statements()

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == EToken.ERROR:
            self.error()

    # Non terminal methods for the contaxt free grammar: statements, statement, expr, term, factor
    def statements(self):
        if self.curr_token.token_code == EToken.END:
            print() 
        if self.curr_token.token_code in [EToken.ID, EToken.PRINT]:
            self.statement()
            if self.curr_token.token_code == EToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error()
        elif self.curr_token.token_code != EToken.END:
            self.error()

    def statement(self):
        if self.curr_token.token_code == EToken.ID:
            var_name = self.curr_token.lexeme
            self.next_token()
            if self.curr_token.token_code == EToken.ASSIGN:
                self.next_token()
                print(f"PUSH {var_name}")
                self.expr()
                print(f"ASSIGN")
            else:
                self.error()
        elif self.curr_token.token_code == EToken.PRINT:
            self.next_token()
            if self.curr_token.token_code == EToken.ID:
                print(f"PUSH {self.curr_token.lexeme}")
                print("PRINT")
                self.next_token()
            else:
                self.error()

    def expr(self):
        self.term()
        while self.curr_token.token_code in [EToken.PLUS, EToken.MINUS]:
            op = self.curr_token.token_code
            self.next_token()
            if self.curr_token.token_code not in [EToken.INT, EToken.ID, EToken.LPAREN]:
                self.error("Syntax error")
                quit(1)
            self.term()
            if op == EToken.PLUS:
                print("ADD")
            else:
                print("SUB")

    def term(self):
        self.factor()
        while self.curr_token.token_code == EToken.MULT:
            self.next_token()
            self.factor()
            print("MULT")

    def factor(self):
        if self.curr_token.token_code == EToken.INT or self.curr_token.token_code == EToken.ID:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()
        elif self.curr_token.token_code == EToken.LPAREN:
            self.next_token()
            self.expr()
            if self.curr_token.token_code == EToken.RPAREN:
                self.next_token()
            else:
                self.error()
        else:
            self.error()

    def error(self, msg="Syntax error"):
        print(msg)
        print()
        #sys.exit(1)
        quit(1)"""

