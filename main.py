from pystrict import Integer, Real, Char, CharArray, List, Dict


def main(args, argv):
	# Примеры работы с Integer
	x = Integer(10)
	y = Integer(5)

	print(f"Integer Addition: {x} + {y} = {x + y}")

	# Примеры работы с Real
	z = Real(3.5)
	print(f"Real Addition: {z} + {Real(2.5)} = {z + Real(2.5)}")

	# Примеры работы с Char и CharArray
	char1 = Char('A')
	char2 = Char('B')
	array = CharArray([char1, char2])
	print(f"CharArray: {array}")


	# Примеры работы с List
	my_list = List()
	my_list.append(x)
	my_list.append(char1)
	print(f"List: {my_list}")

	# Примеры работы с Dict
	my_dict = Dict()
	my_dict.set(char1, x)
	print(f"Dict: {my_dict}, Value for {char1}: {my_dict.get(char1)}")


if __name__ == "__main__":
	main()
