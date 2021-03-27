from abc import ABC, abstractmethod
from typing import Optional

from src.fox.intrepreter.tokens.token import Token


class AbstractTokenScanner(ABC):
    @abstractmethod
    def accept(self, char: str) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def to_token(self, char: str) -> Optional[Token]:
        raise NotImplementedError()
