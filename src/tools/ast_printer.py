from src.fox.intrepreter.syntax_expressions.binary import Binary
from src.fox.intrepreter.syntax_expressions.expr import Expr, Visitor
from src.fox.intrepreter.syntax_expressions.grouping import Grouping
from src.fox.intrepreter.syntax_expressions.literal import Literal
from src.fox.intrepreter.syntax_expressions.unary import Unary
from src.fox.intrepreter.tokens.token import Token
from src.fox.intrepreter.tokens.token_posinion import TokenPosition
from src.fox.intrepreter.tokens.token_type import TokenType


class AstPrinter(Visitor[str]):
    def plot(self, expr: Expr):
        return expr.accept(self)

    def _parenthesize(self, name: str, *expressions: Expr):
        result = f"({name}"

        for expr in expressions:
            result += f" {expr.accept(self)}"

        result += ")"

        return result

    def visit_binary_expr(self, expr: "Binary") -> str:
        return self._parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_unary_expr(self, expr: "Unary") -> str:
        return self._parenthesize(expr.operator.lexeme, expr.left)

    def visit_literal_expr(self, expr: "Literal") -> str:
        return str(expr.value) if expr.value is not None else "nil"

    def visit_grouping_expr(self, expr: "Grouping") -> str:
        return self._parenthesize("group", expr.expression)


if __name__ == "__main__":
    printer = AstPrinter()
    pos = TokenPosition(1, 1, 1)

    expression = Binary(
        Unary(Literal(123), Token(TokenType.MINUS, "-", None, pos)),
        Token(TokenType.STAR, "*", None, pos),
        Grouping(Literal(45.76)),
    )

    print(printer.plot(expression))
