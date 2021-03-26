from abc import ABC, abstractmethod
from typing import TypeVar, Generic


T = TypeVar('T')


class Visitor(ABC, Generic[T]):

	@abstractmethod
	def visit_binary_expr(self, expr: 'Binary') -> T:
		...

	@abstractmethod
	def visit_unary_expr(self, expr: 'Unary') -> T:
		...

	@abstractmethod
	def visit_literal_expr(self, expr: 'Literal') -> T:
		...

	@abstractmethod
	def visit_grouping_expr(self, expr: 'Grouping') -> T:
		...


class Expr(ABC):

	@abstractmethod
	def accept(self, visitor: Visitor[T]) -> T:
		...
