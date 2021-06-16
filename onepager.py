"""
Python 3 OnePager for Python 3.9.x+
By Shay Ellison (the.digital.shay@gmail.com)

You can import this file into Python or run it with python.
python onepager.py

This is a multiline comment / docstring
"""
# This is a single line comment

# Imports
import math                                     # Import the math module
from dataclasses import dataclass               # Import dataclass from the dataclasses module
from typing import (                            # Import multiple items from the typing module
    Any, List, Set, Dict
)
# from . import module_or_package               # Relative import, within a same package
# from .. import module_or_package              # Relative import, within a same container package


# Hello, world
print("Hello, world!")                          # Prints Hello, world!


# Integers (int)
pos_int = 128
neg_int = -128
an_int: int = 1                                 # Typehint, optional

int_add = 1 + 2                                 # = 3
int_sub = 2 - 1                                 # = 1
int_mul = 3 * 4                                 # = 12
int_exp = 2**3                                  # = 8
int_div = 4 // 2                                # = 2, there's a / too but for float (see below)
int_div = 5 // 2                                # = 2
int_mod = 5 % 2                                 # = 5 - 4 = 1
type(pos_int) == int                            # = True


# Floats (float)
pos_float = 4.5
neg_float = -4.5
a_float: float = 4.5                            # Typehint, optional

float_add = 1.0 + 2                             # = 3.0
float_sub = 2.0 - 1                             # = 1.0
float_mul = 3.0 * 4                             # = 12.0
float_exp = 2**-1                               # = 0.5
float_div = 4 / 2                               # = 2.0
float_div = 5 / 2                               # = 2.5
float_div = 7.0 / 2.0                           # = 3.5
float_mod = 4.5 % 2                             # = 4.5 - 4 = 0.5
type(pos_float) == float                        # = True


# Strings (str)
standard_string = "string"
standard_string = 'string'
standard_string = """string"""                  # Triple quotes for multi-line strings but also work for single strings
standard_string = '''string'''                  # Ditto
standard_char = "c"                             # No char type, only string of length 1
standard_char = 'c'
a_string: str = "string"                        # Typehint, optional
a_string: str = 'string'

concat_string = "string" + "c"                  # "stringc"
ss_char = standard_string[0]                    # "s"
format_string1 = f"format {ss_char}"            # "format s" 
format_string1 = f"format {pos_int}"            # "format 128" 
format_string2 = "format %s" % ss_char          # "format s"
format_string2 = "format %d" % pos_int          # "format 128"
format_string3 = "format {}".format(ss_char)    # "format s"
format_string3 = "format {}".format(pos_int)    # "format 128"

# Encoding (translation from characters (utf-8 or otherwise) to bytes) / Decoding (bytes to characters)
std_string = standard_string                    # = "string"
type(std_string) == str                         # = True
std_bytes = std_string.encode('utf-8')          # = b'string', encoded to bytes with utf-8 codec. Value is only returned
                                                #  so must be assigned to a var to capture it.
type(std_bytes) == bytes                        # = True

std_string = std_bytes.decode('utf-8')          # = "string", decoded to string with utf-8 codec
type(std_string) == str                         # = True


# Booleans (bool)
standard_bool = True
standard_bool = False
a_bool: bool = True                             # Typehint, optional
a_bool: bool = False

True or False                                   # = True
True and True                                   # = True
1 == 1                                          # = True
1 != 1                                          # = False
1 < 2                                           # = True
1 > 2                                           # = False
standard_bool is None                           # = False, comparison by reference
standard_bool is not None                       # = True
type(standard_bool) == bool                     # = True

x = ['a', 'b', 'c']
y = x                                           # x and y reference the same object
z = ['a', 'b', 'c']                             # x and z reference different objects with identical data
x is y                                          # = True, comparison by (memory) reference
x is z                                          # = False, comparison by (memory) reference
x == z                                          # = True, comparison by value
x = ['c', 'c', 'c']                             # = Reassign x to a new object
x is y                                          # = False, y still points to original object


# Lists (list)
empty_list = []
list_ints = [1, 2, 3]
list_mixed = [1, "2", 3]
new_list = list()                               # Alternative initialization
a_list: List[Any] = []
int_list: List[int] = [1, 2, 3]                 # Typehint, optional
str_list: List[str] = ["1", "string", "A"]

empty_list.append(1)                            # [1]
empty_list[0]                                   # = 1
1 in empty_list                                 # = True
2 not in empty_list                             # = True
empty_list[0] = 2                               # [2], replaced value at index 0
2 in empty_list                                 # = True
empty_list.remove(2)                            # []
empty_list + [1, 2]                             # = [1, 2]
sorted([2, 5, 1, 4])                            # = [1, 2, 4, 5]
type(empty_list) == list                        # = True


# Tuple (tuple)
empty_tuple = ()
one_tuple = (9,)
two_tuple = (1,2)

one_tuple[0]                                    # = 9, index into tuple like a list
9 in one_tuple
try:
    one_tuple[0] = 1                            # This is not allowed
except TypeError:
    print("Tuples are immutable")
type(one_tuple) == tuple                        # = True


# Dicts (dict)
empty_dict = {}
simple_dict = {
    "key1": 1,
    "key2": 2,
}
mixed_dict = {
    "key1": 1,
    1: "key1",
}
new_dict = dict()                               # Alternative initialization
a_dict: Dict[Any, Any] = {}                     # Typehint, optional
str_int_dict: Dict[str, int] = {}

simple_dict["key3"]= 3
"key3" in simple_dict                           # = True
simple_dict["key3"]                             # = 3
type(simple_dict) == dict                       # = True


# Sets (set)
empty_set = set()                               # NOTE: Just {} is a dict
simple_set = { 1, 2, 3, 4 }
mixed_set = { 1, '2', 3, '4' }
a_set: Set[Any] = set()
int_set: Set[int] = { 1, 2, 3, 4 }

simple_set.add(5)                               # { 1, 2, 3, 4, 5 }
5 in empty_set                                  # = True
simple_set.remove(5)                            # { 1, 2, 3, 4 }
simple_set.union({ 5 })                         # { 1, 2, 3, 4, 5 }
simple_set.intersection({ 1, 2 })               # { 1, 2 }
type(simple_set) == set                         # = True


# Branching
condition = 1
if (condition < 1):
    print("This won't print because the condition isn't met.")
elif (condition > 1):
    print("Ditto. elif short for else if")
else:
    print("This will print because the above conditions weren't met.")

that = False
var = "that" if that else "this"                # "this"


# Looping
i = 0
while i < 10:
    i += 1

nums = [1, 2, 3, 4]
for num in nums:
    print(num)                                  # Prints 1-4, one num per line

for i in range(0, 10):                          # Note in range(start, end) - start is inclusive, end is exclusive
    print(i)

for i in range(10):                             # Identical output as above - start value is optional and 0 by default
    print(i)


# Files
read_file = open("onepager.py", "r")
contents = read_file.read()
print(f"Num chars: {len(contents)}")
read_file.close()                               # Without context manager, close file

with open("onepager.py", "r") as cm_file:       # File opened within a context manager
    lines = cm_file.readlines()
    print(f"Num lines: {len(lines)}")


# Functions
def function_with_no_args():
    """This is a function with no args
    and this multiline string is a doc string
    used to add a comment for the function.
    """
    print("no args")

function_with_no_args()                         # Prints no args : Returns None
type(function_with_no_args)                     # = <class 'function'>, function is a class


def f_with_args(arg1, arg2):
    print(arg1, arg2)
    return arg1

f_with_args(1, 2)                               # Prints 1, 2 : Returns 1


def f_typehinted(arg1: int, arg2: str) -> str:  # Will return a str
    print(arg1, arg2)
    return arg2

f_typehinted(1, "string")                       # Prints 1, string : Returns "string"


def f_w_kwarg(arg1, kwarg1="kwarg1"):
    print(arg1, kwarg1)

f_w_kwarg(1)                                    # Prints 1, kwarg1 : Returns None
f_w_kwarg(1, kwarg1="other1")                   # Prints 1, other1 : Returns None


def f_w_var_args_kwargs(*args, **kwargs):
    print(args, kwargs)    

f_w_var_args_kwargs()                           # Prints () {}
f_w_var_args_kwargs(1, "a", kw1="b", kw2=2)     # Prints (1, "a") {'kw1': 'b', 'kw2': 2}


# Try/Except/Else
d = {'a': 1}
try:
    print("We'll try to grab 'a' from d")
    print(d['a'])
except KeyError:
    print("'a' exists so no error will be thrown.")
else:
    print("We tried and were successful.")

try:
    print("Now we'll try 'b' from d")
    print(d['b'])
except KeyError as e:                           # We can put the error into a var with 'as'
    print("'b' doesn't exist so we got a KeyError")
    print(e)
else:
    print("This won't print since got error.")


def function_with_error():
    raise ValueError("I ony raise a ValueError")

try:
    function_with_error()
except ValueError as ve:    
    print(dir(ve))
    print("ValueError: Got the ValueError")
    print(ve)
    type(ve) == ValueError                      # = True


# Classes
class Example:
    def __init__(self, constructor_arg1: str):
        self.member_var1 = constructor_arg1

    def __str__(self) -> str:
        """Convert an instance of Example to a string"""
        return f"{self.member_var1}"

    def say_hi(self):
        return f"hi, {self.member_var1}"

example = Example("value")
print(str(example))                             # Prints "value"
example.member_var1 = "new value"
print(str(example))                             # Prints "new value"
print(example.say_hi())                         # Prints "hi, new value"
type(example) == Example                        # = True


# Data Classes
@dataclass
class DataClass:
    member1: int                                # Typehints are mandatory for data classes but not actually enforced at
    member2: float                              #  runtime since Python is dynamically typed. Use varous tools (e.g.,
    member3: str                                #  MyPy) to check that what is passed matches the suggested data type.

ds = DataClass(1, 2.0, "3")
type(ds) == DataClass                           # = True
