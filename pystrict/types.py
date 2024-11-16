from .exceptions import TypeErrorException, ValueErrorException


class AbstractType:
	"""Базовый класс для всех пользовательских типов."""
	
	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		raise NotImplementedError("Subclasses should implement this method.")

	def __eq__(self, other):
		raise NotImplementedError("Subclasses should implement this method.")


class Integer(AbstractType):
	__slots__ = ('_value',)

	def __init__(self, value):
		if not isinstance(value, int):
			raise TypeErrorException(f"Expected 'int', got '{type(value).__name__}'")
		self._value = value

	def __add__(self, other):
		self._validate_type(other, Integer)
		return Integer(self._value + other._value)

	def __sub__(self, other):
		self._validate_type(other, Integer)
		return Integer(self._value - other._value)

	def __mul__(self, other):
		self._validate_type(other, Integer)
		return Integer(self._value * other._value)

	def __truediv__(self, other):
		self._validate_type(other, Integer)
		if other._value == 0:
			raise ValueErrorException("Division by zero is not allowed")
		return Real(self._value / other._value)

	def _validate_type(self, other, expected_type):
		if not isinstance(other, expected_type):
			raise TypeErrorException(f"Expected '{expected_type.__name__}', got '{type(other).__name__}'")

	def __repr__(self):
		return f"Integer({self._value})"

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class Real(AbstractType):
	__slots__ = ('_value',)

	def __init__(self, value):
		if not isinstance(value, (float, int)):
			raise TypeErrorException(f"Expected 'float', got '{type(value).__name__}'")
		self._value = float(value)

	def __add__(self, other):
		self._validate_type(other, Real)
		return Real(self._value + other._value)

	def __sub__(self, other):
		self._validate_type(other, Real)
		return Real(self._value - other._value)

	def _validate_type(self, other, expected_type):
		if not isinstance(other, expected_type):
			raise TypeErrorException(f"Expected '{expected_type.__name__}', got '{type(other).__name__}'")

	def __repr__(self):
		return f"Real({self._value})"

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class Char(AbstractType):
	__slots__ = ('_value',)

	def __init__(self, value):
		if not isinstance(value, str) or len(value) != 1:


			raise TypeErrorException("Expected a single character string")
		self._value = value

	def __repr__(self):
		return f"Char('{self._value}')"

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class CharArray(AbstractType):
	__slots__ = ('_values',)

	def __init__(self, values):
		if not all(isinstance(v, Char) for v in values):
			raise TypeErrorException("All elements must be Char")
		self._values = tuple(values)

	def __getitem__(self, index):
		self._validate_index(index)
		return self._values[index]

	def _validate_index(self, index):
		if not isinstance(index, int) or index < 0 or index >= len(self._values):
			raise IndexError("Index out of range")

	def __len__(self):
		return len(self._values)

	def __repr__(self):
		return f"Array({self._values})"

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class List(AbstractType):
	__slots__ = ('_values',)

	def __init__(self, values = []):
		self._values = values

	def append(self, value):
		if not isinstance(value, (Integer, Char)):
			raise TypeErrorException("Expected 'Integer' or 'Char'")
		self._values.append(value)

	def __getitem__(self, index):
		self._validate_index(index)
		return self._values[index]

	def _validate_index(self, index):
		if not isinstance(index, int) or index < 0 or index >= len(self._values):
			raise IndexError("Index out of range")

	def __len__(self):
		return len(self._values)

	def __repr__(self):
		return f"List({self._values})"

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class Dict(AbstractType):
	__slots__ = ('_values',)

	def __init__(self, values = {}):
		self._values = values

	def set(self, key: Char, value: Integer):
		if not isinstance(key, Char):
			raise TypeErrorException("Key must be Char")
		if not isinstance(value, Integer):
			raise TypeErrorException("Value must be Integer")
		self._values[str(key)] = value

	def get(self, key: Char) -> Integer:
		if not isinstance(key, Char):
			raise TypeErrorException("Key must be Char")
		return self._values.get(str(key), None)

	def __repr__(self):
		return f"Dict({self._values})"

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class Boolean(AbstractType):
	__slots__ = ('_value',)

	def __init__(self, value):
		if not isinstance(value, bool):
			raise TypeErrorException(f"Expected 'bool', got '{type(value).__name__}'")
		self._value = value

	def __repr__(self):
		return f"Boolean({self._value})"

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class ShortInt(Integer):
	def __init__(self, value):
		super().__init__(value)
		if not (-32768 <= value <= 32767):
			raise ValueErrorException("Value out of range for ShortInt")

def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')


class LongInt(Integer):
	def __init__(self, value):
		super().__init__(value)
		if not (-9223372036854775808 <= value <= 9223372036854775807):
			raise ValueErrorException("Value out of range for LongInt")

	def __eq__(self, other):
		if type(other) == type(self._value) and other == self._value:
			return True
		else:
			raise TypeErrorException(f'Type error: {type(self._value)} and {type(other)}')
