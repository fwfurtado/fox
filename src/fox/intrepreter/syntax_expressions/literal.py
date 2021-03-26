from typing import Any

from fox.intrepreter.syntax_expressions.expr import Expr, Visitor


class Literal(Expr):
	def __init__(self, value: Any):
		self.__value = value

	@property
	def value(self) -> Any:
		return self.__value

	def accept(self, visitor: Visitor['Literal']) -> 'Literal':
		return visitor.visit_literal_expr(self)