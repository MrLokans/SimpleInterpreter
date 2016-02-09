INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class InterpreterParsingError(Exception):
    pass


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return '<Token({}: {})>'.format(self.type, self.value)

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.text_position = 0
        self.current_token = None
        self.current_char = self.text[self.text_position]

    def advance(self):
        """Advance pointer to the current symbol and its value"""
        self.text_position += 1
        if self.text_position > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.text_position]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def consume_integer(self):
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
                return Token(INTEGER, self.consume_integer())

            if self.current_char == "+":
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            raise InterpreterParsingError()
        return Token(EOF, None)

    def eat_token(self, token_type):

        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            raise InterpreterParsingError()

    def expr(self):

        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat_token(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat_token(PLUS)
        else:
            self.eat_token(MINUS)

        right = self.current_token
        self.eat_token(INTEGER)

        if op.type == MINUS:
            result = left.value - right.value

        else:
            result = left.value + right.value

        return result


def main():
    while True:
        text = input(">")
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
