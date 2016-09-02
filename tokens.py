INTEGER, PLUS, MINUS, MUL, DIV, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF'
)


class Token(object):
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value

    def __str__(self):
        return '<Token({}: {})>'.format(self.type, self.value)

    def __repr__(self):
        return self.__str__()
