import tokens


class LexerError(Exception):
    pass


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise LexerError("Invalid character")

    def advance(self):
        """Move current_char pointer to he next character
        """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def consume_integer(self):
        """Read multiple-digit integer from the text"""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Tokenizer method, that splits text into token sequence"""

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return tokens.Token(tokens.INTEGER, self.consume_integer())

            if self.current_char == "+":
                self.advance()
                return tokens.Token(tokens.PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return tokens.Token(tokens.MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return tokens.Token(tokens.MUL, '*')

            if self.current_char == '/':
                self.advance()
                return tokens.Token(tokens.DIV, '/')

            if self.current_char == '(':
                self.advance()
                return tokens.Token(tokens.LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return tokens.Token(tokens.RPAREN, ')')

            self.error()

        return tokens.Token(tokens.EOF, None)
