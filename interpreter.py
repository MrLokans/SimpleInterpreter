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

    def get_next_token(self):
        """Tokenizer method, that splits text into token sequence"""

        # If we encounter last symbol it means we reached the end of the text
        if self.text_position > len(self.text) - 1:
            return Token(EOF, None)

        current_char = self.text[self.text_position]

        # handle integer tokenization
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.text_position += 1
            return token
        if current_char == "+":
            token = Token(PLUS, current_char)
            self.text_position += 1
            return token

        if current_char == "-":
            token = Token(PLUS, current_char)
            self.text_position += 1
            return token

        # if symbol is not identified - exit with error
        raise InterpreterParsingError()

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
        self.eat_token(PLUS)

        right = self.current_token
        self.eat_token(INTEGER)

        if op.type == MINUS:
            result = left.value - right.value

        if op.type == PLUS:
            result = left.value - right.value

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
