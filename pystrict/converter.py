from .types import Integer, Real
from .exceptions import TypeErrorException


class TypeConverter:
	@staticmethod
	def to_integer(obj) -> Integer:
		if isinstance(obj, Integer):
			return obj
		elif isinstance(obj, (int, bool)):
			return Integer(obj)

		raise TypeErrorException(f"Cannot convert {type(obj).__name__} to Integer")

	@staticmethod
	def to_real(obj) -> Real:
		if isinstance(obj, Real):
			return obj
		elif isinstance(obj, Integer):
			return Real(float(obj._value))

		raise TypeErrorException(f"Cannot convert {type(obj).__name__} to Real")
		