from typing import Optional

from fox.intrepreter.scanners.scanner_mixin import ScannerMixin
from fox.intrepreter.scanners.token_scanner.abstract_token_scanner import AbstractTokenScanner
from fox.intrepreter.tokens.token import Token
from fox.intrepreter.tokens.token_type import TokenType


class StaticTokenScanner(AbstractTokenScanner):
    ACCEPTED_TOKENS = {
        "(", ")",
        "{", "}",
        ",", ".",
        "-", "+", ";", "*"

    }

    TOKEN_DICT = {
        "(": TokenType.LEFT_PAREN,
        ")": TokenType.RIGHT_PAREN,
        "{": TokenType.LEFT_BRACE,
        "}": TokenType.RIGHT_BRACE,
        ",": TokenType.COMMA,
        ".": TokenType.DOT,
        "-": TokenType.MINUS,
        "+": TokenType.PLUS,
        ";": TokenType.SEMICOLON,
        "*": TokenType.STAR,
    }

    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char in StaticTokenScanner.ACCEPTED_TOKENS

    def to_token(self, char: str) -> Optional[Token]:
        token_type = StaticTokenScanner.TOKEN_DICT.get(char)
        lexeme = self.__mixin.lexeme()
        position = self.__mixin.position()

        return Token(token_type, lexeme, None, position)
