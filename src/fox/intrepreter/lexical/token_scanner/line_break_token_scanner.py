from typing import Optional

from src.fox.intrepreter.lexical.scanner_mixin import ScannerMixin
from src.fox.intrepreter.lexical.token_scanner.abstract_token_scanner import (
    AbstractTokenScanner,
)
from src.fox.intrepreter.tokens.token import Token


class LineBreakTokenScanner(AbstractTokenScanner):
    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char == "\n"

    def to_token(self, char: str) -> Optional[Token]:
        self.__mixin.advance()
        return None
