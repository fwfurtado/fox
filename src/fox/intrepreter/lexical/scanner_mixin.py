from abc import ABC

from src.fox.intrepreter.tokens.token_posinion import TokenPosition


class ScannerMixin(ABC):
    def peek(self) -> str:
        raise NotImplementedError()

    def peek_next(self) -> str:
        raise NotImplementedError()

    def lexeme(self):
        raise NotImplementedError()

    def match(self, char: str) -> bool:
        raise NotImplementedError()

    def position(self) -> TokenPosition:
        raise NotImplementedError()

    def eof(self) -> bool:
        raise NotImplementedError()

    def advance(self):
        raise NotImplementedError()

    def skip(self):
        raise NotImplementedError()

    def new_line(self):
        raise NotImplementedError()
