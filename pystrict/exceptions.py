class InitializationError(Exception):
	"""Исключение, вызванное отсутствием точки доступа."""
	pass


class TypeErrorException(Exception):
	"""Вызвано при ошибке типа данных."""
	pass


class ValueErrorException(Exception):
	"""Вызвано при недопустимом значении."""
	pass
