from typing import Optional, Dict, Set

from src.fox.intrepreter.lexical.scanner_mixin import ScannerMixin
from src.fox.intrepreter.lexical.token_scanner.abstract_token_scanner import (
    AbstractTokenScanner,
)
from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.tokens.token_type import TokenType


class StaticTokenScanner(AbstractTokenScanner):
    ACCEPTED_TOKENS: Set[str] = {"(", ")", "{", "}", ",", ".", "-", "+", ";", "*"}

    TOKEN_DICT: Dict[str, TokenType] = {
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
        token_type = StaticTokenScanner.TOKEN_DICT[char]
        lexeme = self.__mixin.lexeme()
        position = self.__mixin.position()

        return Token(token_type, lexeme, None, position)
