from fox.intrepreter.syntax_expressions.expr import Expr, Visitor


class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.__expression = expression

	@property
	def expression(self) -> Expr:
		return self.__expression

	def accept(self, visitor: Visitor['Grouping']) -> 'Grouping':
		return visitor.visit_grouping_expr(self)