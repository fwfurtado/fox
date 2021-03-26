from typing import Optional

from fox.intrepreter.scanners.scanner_mixin import ScannerMixin
from fox.intrepreter.scanners.token_scanner.abstract_token_scanner import AbstractTokenScanner
from fox.intrepreter.tokens.token import Token
from fox.intrepreter.tokens.token_type import TokenType


class IdentifierTokenScanner(AbstractTokenScanner):
    KEYWORDS = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "fun": TokenType.FUN,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "not": TokenType.NOT,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE,
    }

    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return self._is_alpha(char)

    def to_token(self, char: str) -> Optional[Token]:
        while self._is_alpha_numeric(self.__mixin.peek()):
            self.__mixin.advance()

        lexeme = self.__mixin.lexeme()
        position = self.__mixin.position()
        token_type = self.KEYWORDS.get(lexeme, TokenType.IDENTIFIER)

        return Token(token_type, lexeme, None, position)

    @staticmethod
    def _is_alpha_numeric(char: str) -> bool:
        return IdentifierTokenScanner._is_digit(char) or IdentifierTokenScanner._is_alpha(char)

    @staticmethod
    def _is_alpha(char: str) -> bool:
        return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == "_"

    @staticmethod
    def _is_digit(char: str) -> bool:
        return '0' <= char <= '9'
