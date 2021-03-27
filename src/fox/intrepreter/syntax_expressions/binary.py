from __future__ import annotations

from src.fox.intrepreter.syntax_expressions.expr import Expr, Visitor
from src.fox.intrepreter.tokens.token import Token


class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.__left = left
        self.__operator = operator
        self.__right = right

    @property
    def left(self) -> Expr:
        return self.__left

    @property
    def operator(self) -> Token:
        return self.__operator

    @property
    def right(self) -> Expr:
        return self.__right

    def accept(self, visitor: Visitor[Binary]) -> Binary:  # type: ignore[override]
        return visitor.visit_binary_expr(self)
