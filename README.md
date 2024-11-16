# pystrictio
Python, but strict typing (fun project)

## Example

```python
from pystrict import Integer, Real, Char, CharArray, List, Dict


def main(args, argv):
	x = Integer(10)
	y = Integer(5)

	print(f"Integer Addition: {x} + {y} = {x + y}")

	z = Real(3.5)
	print(f"Real Addition: {z} + {Real(2.5)} = {z + Real(2.5)}")

	char1 = Char('A')
	char2 = Char('B')
	array = CharArray([char1, char2])
	print(f"CharArray: {array}")

	my_list = List()
	my_list.append(x)
	my_list.append(char1)
	print(f"List: {my_list}")

	my_dict = Dict()
	my_dict.set(char1, x)
	print(f"Dict: {my_dict}, Value for {char1}: {my_dict.get(char1)}")


if __name__ == "__main__":
	main()
```

Launch:

```bash
 $ python3 -m pystrict main.py

Integer Addition: Integer(10) + Integer(5) = Integer(15)
Real Addition: Real(3.5) + Real(2.5) = Real(6.0)
CharArray: Array((Char('A'), Char('B')))
List: List([Integer(10), Char('A')])
Dict: Dict({"Char('A')": Integer(10)}), Value for Char('A'): Integer(10)
```

## Invalid example

```python
from pystrict import Integer, Real, Char, CharArray, List, Dict

x = Integer(10)
y = Integer(5)

print(f"Integer Addition: {x} + {y} = {x + y}")

z = Real(3.5)
print(f"Real Addition: {z} + {Real(2.5)} = {z + Real(2.5)}")

char1 = Char('A')
char2 = Char('B')
array = CharArray([char1, char2])
print(f"CharArray: {array}")

my_list = List()
my_list.append(x)
my_list.append(char1)
print(f"List: {my_list}")

my_dict = Dict()
my_dict.set(char1, x)
print(f"Dict: {my_dict}, Value for {char1}: {my_dict.get(char1)}")
```

Launch:

```bash
 $ python3 -m pystrict failed_main.py


Integer Addition: Integer(10) + Integer(5) = Integer(15)
Real Addition: Real(3.5) + Real(2.5) = Real(6.0)
CharArray: Array((Char('A'), Char('B')))
List: List([Integer(10), Char('A')])
Dict: Dict({"Char('A')": Integer(10)}), Value for Char('A'): Integer(10)
Traceback (most recent call last):
  File "/home/alexeev/Desktop/Projects/pystrictio/pystrict/__main__.py", line 23, in launch
    return config_module.main(Integer(len(sys.argv)), List(sys.argv))
           ^^^^^^^^^^^^^^^^^^
AttributeError: module 'failed_main' has no attribute 'main'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/alexeev/Desktop/Projects/pystrictio/pystrict/__main__.py", line 37, in <module>
    main(len(sys.argv), sys.argv)
  File "/home/alexeev/Desktop/Projects/pystrictio/pystrict/__main__.py", line 33, in main
    launch(argv[1])
  File "/home/alexeev/Desktop/Projects/pystrictio/pystrict/__main__.py", line 25, in launch
    raise Exception(f'program entry point not found: main(argc, argv) does not exist. Message: {ex}')
Exception: program entry point not found: main(argc, argv) does not exist. Message: module 'failed_main' has no attribute 'main'
```
