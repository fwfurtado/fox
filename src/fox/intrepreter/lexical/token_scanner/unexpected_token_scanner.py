from typing import Optional

from fox.intrepreter.scanners.token_scanner.abstract_token_scanner import AbstractTokenScanner
from fox.intrepreter.tokens.token import Token


class UnexpectedTokenScanner(AbstractTokenScanner):
    def accept(self, char: str) -> bool:
        return True

    def to_token(self, char: str) -> Optional[Token]:
        raise
