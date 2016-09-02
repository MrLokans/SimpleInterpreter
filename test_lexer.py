import pytest

from lexer import Lexer


def test_lexer_extracts_single_integer():
    text = "11"

    l = Lexer()
    l.lex(text)

    assert l.get_next_token().value == 11


def test_lexer_extracts_integer_with_spaces():
    text = "  11 "

    l = Lexer()
    l.lex(text)
    assert l.get_next_token().value == 11


@pytest.mark.parametrize("test_input, expected_value", [
    (' - ', '-'),
    ('  + ', '+'),
    ('  * ', '*'),
    ('\t /\t', '/'),
])
def test_lexer_extracts_signs(test_input, expected_value):
    l = Lexer()
    l.lex(test_input)
    assert l.get_next_token().value == expected_value
