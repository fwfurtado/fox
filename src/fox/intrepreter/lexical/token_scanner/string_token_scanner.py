from typing import Optional

from src.fox.intrepreter.lexical.scanner_mixin import ScannerMixin
from src.fox.intrepreter.lexical.token_scanner.abstract_token_scanner import (
    AbstractTokenScanner,
)
from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.tokens.token_type import TokenType


class StringTokenScanner(AbstractTokenScanner):
    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char == '"'

    def to_token(self, char: str) -> Optional[Token]:
        while self.__mixin.peek() != '"' and not self.__mixin.eof():

            if self.__mixin.peek() == "\n":
                self.__mixin.new_line()
            else:
                self.__mixin.advance()

        if self.__mixin.eof():
            raise

        self.__mixin.advance()

        lexeme = self.__mixin.lexeme()
        literal = lexeme[1 : len(lexeme) - 1]
        position = self.__mixin.position()

        return Token(TokenType.STRING, lexeme, literal, position)
