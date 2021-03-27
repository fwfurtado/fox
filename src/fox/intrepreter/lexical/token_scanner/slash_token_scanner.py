from typing import Optional

from src.fox.intrepreter.lexical.scanner_mixin import ScannerMixin
from src.fox.intrepreter.lexical.token_scanner.abstract_token_scanner import (
    AbstractTokenScanner,
)
from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.tokens.token_type import TokenType


class SlashTokenScanner(AbstractTokenScanner):
    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char == "/"

    def to_token(self, char: str) -> Optional[Token]:
        if self.__mixin.match("/"):
            while self.__mixin.peek() != "\n" and not self.__mixin.eof():
                self.__mixin.advance()
            return None
        else:
            token_type = TokenType.SLASH
            lexeme = self.__mixin.lexeme()
            position = self.__mixin.position()

            return Token(token_type, lexeme, char, position)
