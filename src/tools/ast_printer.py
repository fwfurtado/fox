from typing import List

from fox.intrepreter.syntax_expressions.binary import Binary
from fox.intrepreter.syntax_expressions.expr import Visitor, Expr
from fox.intrepreter.syntax_expressions.grouping import Grouping
from fox.intrepreter.syntax_expressions.literal import Literal
from fox.intrepreter.syntax_expressions.unary import Unary
from fox.intrepreter.tokens.token import Token
from fox.intrepreter.tokens.token_posinion import TokenPosition
from fox.intrepreter.tokens.token_type import TokenType


class AstPrinter(Visitor[str]):

    def print(self, expr: Expr):
        return expr.accept(self)

    def _parenthesize(self, name: str, *exprs: List[Expr]):
        result = f"({name}"

        for expr in exprs:
            result += f' {expr.accept(self)}'

        result += ")"

        return result

    def visit_binary_expr(self, expr: 'Binary') -> str:
        return self._parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_unary_expr(self, expr: 'Unary') -> str:
        return self._parenthesize(expr.operator.lexeme, expr.left)

    def visit_literal_expr(self, expr: 'Literal') -> str:
        return str(expr.value) if expr.value is not None else "nil"

    def visit_grouping_expr(self, expr: 'Grouping') -> str:
        return self._parenthesize("group", expr.expression)


if __name__ == '__main__':
    printer = AstPrinter()
    pos = TokenPosition(1, 1, 1)

    expression = Binary(
        Unary(
            Literal(123),
            Token(TokenType.MINUS, "-", None, pos)),
        Token(TokenType.STAR, "*", None, pos),
        Grouping(
            Literal(45.76)
        )
    )

    print(printer.print(expression))
