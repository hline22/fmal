from eparser import EParser
from elexer import ELexer
from etoken import EToken

def main():
    lexer = ELexer()
    parser = EParser(lexer)
    parser.parse()

if __name__ == "__main__":
    main()