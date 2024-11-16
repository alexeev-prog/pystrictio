import sys
import importlib
from .types import Integer, List


def dynamic_import(module: str):
	"""
	Dynamic import with importlib

	:param		module:	 The module
	:type		module:	 str

	:returns:	module
	:rtype:		module
	"""
	return importlib.import_module(str(module))


def launch(filename: str):
	config_module = dynamic_import(str(filename).replace(".py", ""))

	try:
		return config_module.main(Integer(len(sys.argv)), List(sys.argv))
	except Exception as ex:
		raise Exception(f'program entry point not found: main(argc, argv) does not exist. Message: {ex}')


def main(argc, argv):
	if argc < 2:
		raise Exception(f'Usage: python3 -m pystrict <file.py>')
		return

	launch(argv[1])


if __name__ == '__main__':
	main(len(sys.argv), sys.argv)
