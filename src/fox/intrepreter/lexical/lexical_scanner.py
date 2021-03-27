from typing import Iterator

from src.fox.intrepreter.lexical.scanner_mixin import ScannerMixin
from src.fox.intrepreter.lexical.token_scanner.bang_token_scanner import (
    BangTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.blank_token_scanner import (
    BlankTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.equal_token_scanner import (
    EqualTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.greater_token_scanner import (
    GreaterTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.identifier_token_scanner import (
    IdentifierTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.less_token_scanner import (
    LessTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.line_break_token_scanner import (
    LineBreakTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.number_token_scanner import (
    NumberTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.slash_token_scanner import (
    SlashTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.static_token_scanner import (
    StaticTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.string_token_scanner import (
    StringTokenScanner,
)
from src.fox.intrepreter.lexical.token_scanner.unexpected_token_scanner import (
    UnexpectedTokenScanner,
)
from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.tokens.token_posinion import TokenPosition
from src.fox.intrepreter.tokens.token_type import TokenType


class Scanner(ScannerMixin):
    def __init__(self, source: str):
        self.__source = source
        self.__current = 0
        self.__start = 0
        self.__line = 1
        self.__end = 0

        self.__token_scanners = [
            StaticTokenScanner(self),
            BangTokenScanner(self),
            LessTokenScanner(self),
            GreaterTokenScanner(self),
            EqualTokenScanner(self),
            SlashTokenScanner(self),
            BlankTokenScanner(self),
            LineBreakTokenScanner(self),
            StringTokenScanner(self),
            NumberTokenScanner(self),
            IdentifierTokenScanner(self),
            UnexpectedTokenScanner(),
        ]

    def __iter__(self) -> Iterator[Token]:
        while not self.eof():
            self.__start = self.__current
            token = self._scan_token()

            if token:
                yield token

        yield Token(TokenType.EOF, "", None, self.position())

    def _scan_token(self):
        read_char = self.advance()
        token_scanner = next(
            filter(lambda ts: ts.accept(read_char), self.__token_scanners)
        )

        return token_scanner.to_token(read_char)

    def eof(self) -> bool:
        return self.__current >= len(self.__source)

    def advance(self):
        self._increment_column()
        return self.__source[self.__current - 1]

    def match(self, expected: str) -> bool:
        if self.eof():
            return False

        if self.peek() != expected:
            return False

        self._increment_column()

        return True

    def peek(self) -> str:
        return "\0" if self.eof() else self.__source[self.__current]

    def peek_next(self) -> str:
        eof = self.__current + 1 >= len(self.__source)

        return "\0" if eof else self.__source[self.__current + 1]

    def new_line(self):
        self.advance()
        self.__line += 1
        self.__end = 1

    def _increment_column(self):
        self.__end += 1
        self.__current += 1

    def skip(self):
        self.__end += 1

    def lexeme(self):
        return self.__source[self.__start : self.__current]

    def position(self) -> TokenPosition:
        length = self.__current - self.__start
        return TokenPosition(self.__line, self.__start + 1, length)
