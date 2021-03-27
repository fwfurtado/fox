from __future__ import annotations

from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.syntax_expressions.expr import Expr, Visitor


class Unary(Expr):
    def __init__(self, left: Expr, operator: Token):
        self.__left = left
        self.__operator = operator

    @property
    def left(self) -> Expr:
        return self.__left

    @property
    def operator(self) -> Token:
        return self.__operator

    def accept(self, visitor: Visitor[Unary]) -> Unary:  # type: ignore[override]
        return visitor.visit_unary_expr(self)
