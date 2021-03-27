from typing import Any

from src.fox.intrepreter.tokens.token_posinion import TokenPosition
from src.fox.intrepreter.tokens.token_type import TokenType


class Token:
    def __init__(
        self, token_type: TokenType, lexeme: str, literal: Any, position: TokenPosition
    ):
        self.__token_type = token_type
        self.__lexeme = lexeme
        self.__literal = literal
        self.__position = position

    @property
    def token_type(self):
        return self.__token_type

    @property
    def lexeme(self):
        return self.__lexeme

    @property
    def literal(self):
        return self.__literal

    @property
    def line(self):
        return self.__position.line

    @property
    def column(self):
        return self.__position.column

    @property
    def length(self):
        return self.__position.length

    def __str__(self):
        return f"Token({self.token_type}, {self.lexeme}, {self.literal}, {self.line}, {self.column}, {self.length})"
