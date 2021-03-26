from typing import Optional

from fox.intrepreter.scanners.scanner_mixin import ScannerMixin
from fox.intrepreter.scanners.token_scanner.abstract_token_scanner import AbstractTokenScanner
from fox.intrepreter.tokens.token import Token
from fox.intrepreter.tokens.token_type import TokenType


class LessTokenScanner(AbstractTokenScanner):

    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char == "<"

    def to_token(self, char: str) -> Optional[Token]:
        token_type = TokenType.LESS_EQUAL if self.__mixin.match("=") else TokenType.LESS
        lexeme = self.__mixin.lexeme()
        position = self.__mixin.position()

        return Token(token_type, lexeme, None, position)
