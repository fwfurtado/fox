from typing import Optional

from src.fox.intrepreter.lexical.scanner_mixin import ScannerMixin
from src.fox.intrepreter.lexical.token_scanner.abstract_token_scanner import (
    AbstractTokenScanner,
)
from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.tokens.token_type import TokenType


class GreaterTokenScanner(AbstractTokenScanner):
    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char == ">"

    def to_token(self, char: str) -> Optional[Token]:
        token_type = (
            TokenType.GREATER_EQUAL if self.__mixin.match("=") else TokenType.GREATER
        )
        lexeme = self.__mixin.lexeme()
        position = self.__mixin.position()

        return Token(token_type, lexeme, None, position)
