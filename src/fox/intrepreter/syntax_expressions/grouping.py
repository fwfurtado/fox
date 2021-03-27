from __future__ import annotations

from src.fox.intrepreter.syntax_expressions.expr import Expr, Visitor


class Grouping(Expr):
    def __init__(self, expression: Expr):
        self.__expression = expression

    @property
    def expression(self) -> Expr:
        return self.__expression

    def accept(self, visitor: Visitor[Grouping]) -> Grouping:  # type: ignore[override]
        return visitor.visit_grouping_expr(self)
