from fox.intrepreter.tokens.token import Token
from fox.intrepreter.syntax_expressions.expr import Expr, Visitor


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

	def accept(self, visitor: Visitor['Binary']) -> 'Binary':
		return visitor.visit_binary_expr(self)