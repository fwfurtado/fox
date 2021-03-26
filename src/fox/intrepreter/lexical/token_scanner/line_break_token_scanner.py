from typing import Optional

from fox.intrepreter.scanners.scanner_mixin import ScannerMixin
from fox.intrepreter.scanners.token_scanner.abstract_token_scanner import AbstractTokenScanner
from fox.intrepreter.tokens.token import Token


class LineBreakTokenScanner(AbstractTokenScanner):

    def __init__(self, mixin: ScannerMixin):
        self.__mixin = mixin

    def accept(self, char: str) -> bool:
        return char == "\n"

    def to_token(self, char: str) -> Optional[Token]:
        self.__mixin.advance()
        return
