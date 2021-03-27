from src.fox.intrepreter.lexical.scanner_mixin import ScannerMixin
from src.fox.intrepreter.lexical.token_scanner.abstract_token_scanner import (
    AbstractTokenScanner,
)
from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.tokens.token_type import TokenType


class BangTokenScanner(AbstractTokenScanner):
    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char == "!"

    def to_token(self, char: str) -> Token:
        if not self.__mixin.match("="):
            raise

        lexeme = self.__mixin.lexeme()
        position = self.__mixin.position()

        return Token(TokenType.BANG_EQUAL, lexeme, None, position)
