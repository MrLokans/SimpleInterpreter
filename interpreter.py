from lexer import Lexer
import tokens

try:
    input = raw_input
except:
    pass


class InterpreterParsingError(Exception):
    pass


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise InterpreterParsingError("Invalid syntax")

    def eat_token(self, token_type):

        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        self.eat_token(tokens.INTEGER)
        return token.value

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.type in (tokens.MUL, tokens.DIV):
            token = self.current_token
            if token.type == tokens.MUL:
                self.eat_token(tokens.MUL)
                result = result * self.factor()
            elif token.type == tokens.DIV:
                self.eat_token(tokens.DIV)
                result = result / self.factor()

        return result

    def expr(self):

        self.current_token = self.lexer.get_next_token()

        result = self.term()
        while self.current_token.type in (tokens.PLUS, tokens.MINUS):
            token = self.current_token
            if token.type == tokens.PLUS:
                self.eat_token(tokens.PLUS)
                result += self.term()
            elif token.type == tokens.MINUS:
                self.eat_token(tokens.MINUS)
                result -= self.term()
        return result


def main():
    while True:
        text = input(">")
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
