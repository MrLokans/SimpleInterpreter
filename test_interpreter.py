import pytest

from interpreter import Interpreter
from lexer import Lexer


@pytest.fixture()
def interpreter():
    return Interpreter(Lexer)


def test_simple_number_input(interpreter):
    text = "1"
    interpreter.eval_text(text)
    result = interpreter.expr()

    assert str(result) == "1"


def test_simple_addition(interpreter):
    text = "1 + 3"
    interpreter.eval_text(text)
    result = interpreter.expr()

    assert str(result) == "4"


def test_simple_subtraction(interpreter):
    text = "1 - 3"
    interpreter.eval_text(text)
    result = interpreter.expr()

    assert str(result) == "-2"


def test_simple_multiplication(interpreter):
    text = "10 *  3"
    interpreter.eval_text(text)
    result = interpreter.expr()

    assert str(result) == "30"


def test_simple_division(interpreter):
    text = "4 / 4"
    interpreter.eval_text(text)
    result = interpreter.expr()

    assert str(result) == "1.0"


def test_parentheses_operations(interpreter):
    text = "1 - (100 / 25) * 4 + (36 * 4 - 13)"
    interpreter.eval_text(text)
    result = interpreter.expr()

    assert str(result) == "116.0"
