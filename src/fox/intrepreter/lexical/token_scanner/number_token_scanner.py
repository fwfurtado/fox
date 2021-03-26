from typing import Optional

from fox.intrepreter.scanners.scanner_mixin import ScannerMixin
from fox.intrepreter.scanners.token_scanner.abstract_token_scanner import AbstractTokenScanner
from fox.intrepreter.tokens.token import Token
from fox.intrepreter.tokens.token_type import TokenType


class NumberTokenScanner(AbstractTokenScanner):

    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return self._is_digit(char)

    def to_token(self, char: str) -> Optional[Token]:
        while self._is_digit(self.__mixin.peek()):
            self.__mixin.advance()

        if self.__mixin.peek() == "." and self._is_digit(self.__mixin.peek_next()):
            self.__mixin.advance()

            while self._is_digit(self.__mixin.peek()):
                self.__mixin.advance()

        lexeme = self.__mixin.lexeme()
        literal = float(lexeme)
        position = self.__mixin.position()

        return Token(TokenType.NUMBER, lexeme, literal, position)

    @staticmethod
    def _is_digit(char: str):
        return '0' <= char <= '9'
