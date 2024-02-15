import sys
from etoken import EToken

class ELexer:
    def __init__(self):
        self.buffer = []

    def read_char(self):
        """Reads the next character from stdin or buffer"""
        if self.buffer:
            return self.buffer.pop(0)  # return the first item from the buffer if it exists
        else:
            return sys.stdin.read(1)  # else, read from stdin

    def unread_char(self, char):
        """Puts a character back into the buffer"""
        self.buffer.insert(0, char)  # inserting the character back at the start of the buffer

    def get_next_token(self):
        lexeme = ''
        while True:
            char = self.read_char()

            if not char:
                return EToken("", EToken.END)  # end of input

            if char.isspace():
                continue  # skip whitespace

            if char.isnumeric():
                lexeme = char
                while True:
                    next_char = self.read_char()
                    if next_char.isnumeric():
                        lexeme += next_char
                    else:
                        self.unread_char(next_char)  # putting the non-numeric char back into the buffer
                        return EToken(lexeme, EToken.INT)

            elif char.isalpha():
                lexeme = char
                while True:
                    next_char = self.read_char()
                    if next_char.isalnum():
                        lexeme += next_char
                    else:
                        self.unread_char(next_char)  # putting the non-alphanumeric char back into the buffer
                        if lexeme == "end":
                            return EToken(lexeme, EToken.END)
                        elif lexeme == "print":
                            return EToken(lexeme, EToken.PRINT)
                        else:
                            return EToken(lexeme, EToken.ID)

            elif char in ['+', '-', '*', '(', ')', '=',';']:
                token_map = {
                    '+': EToken.PLUS,
                    '-': EToken.MINUS,
                    '*': EToken.MULT,
                    '(': EToken.LPAREN,
                    ')': EToken.RPAREN,
                    '=': EToken.ASSIGN,
                    ';': EToken.SEMICOL
                }
                return EToken(char, token_map[char])

            else:
                return EToken(char, EToken.ERROR)

    def create_token(self, lexeme, token_code):
        return EToken(lexeme, token_code)
