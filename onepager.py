"""
This is a multiline comment / docstring
"""
# This is a comment

# Imports
import math                             # Import the math module
from dataclasses import dataclass       # Import dataclass from the typing module
from typing import (                    # Import multiple items from the typing module
    Any, List, Set, Dict
)
# from . import module_or_package       # Relative import, within a package, same level
# from .. import module_or_package      # Relative import, within a container package, previous level

# Hello, world
print("Hello, world!")

# Integers (int)
pos_int = 128
neg_int = -128
an_int: int = 1                         # Typehint, optional

int_add = 1 + 2                         # = 3
int_sub = 2 - 1                         # = 1
int_mul = 3 * 4                         # = 12
int_exp = 2**3                          # = 8
int_div = 4 // 2                        # = 2
int_div = 5 // 2                        # = 2
int_mod = 5 % 2                         # = 5 - 4 = 1


# Floats (float)
pos_float = 4.5
neg_float = -4.5
a_float: float = 4.5                    # Typehint, optional

float_add = 1.0 + 2                     # = 3.0
float_sub = 2.0 - 1                     # = 1.0
float_mul = 3.0 * 4                     # = 12.0
float_exp = 2**-1                       # = 0.5
float_div = 4 / 2                       # = 2.0
float_div = 5 / 2                       # = 2.5
float_div = 7.0 / 2.0                   # = 3.5
float_mod = 4.5 % 2                     # = 4.5 - 4 = 0.5


# Strings (str)
standard_string = "string"
standard_string = 'string'
standard_char = "c"                     # No char type, only string of length 1
standard_char = 'c'
a_string: str = "string"                # Typehint, optional
a_string: str = 'string'

concat_string = "string" + "c"                  # "stringc"
ss_char = standard_string[0]                    # "s"
format_string1 = f"format {ss_char}"            # "format s" 
format_string1 = f"format {pos_int}"            # "format 128" 
format_string2 = "format %s" % ss_char          # "format s"
format_string2 = "format %d" % pos_int          # "format 128"
format_string3 = "format {}".format(ss_char)    # "format s"
format_string3 = "format {}".format(pos_int)    # "format 128"


# Bytes (bytes)
standard_bytes = b"bytestring"
standard_bytes = b'bytestring'


# Booleans (bool)
standard_bool = True
standard_bool = False
a_bool: bool = True
a_bool: bool = False

True or False                                   # = True
True and True                                   # = True
1 == 1                                          # = True
1 != 1                                          # = False
1 < 2                                           # = True
1 > 2                                           # = False
standard_bool is None                           # = False, comparison by reference
standard_bool is not None                       # = True


# Lists (list) ==
empty_list = []
list_ints = [1, 2, 3]
list_mixed = [1, "2", 3]
new_list = list()                   # Alternative initialization
a_list: List[Any] = []
int_list: List[int] = [1, 2, 3]     # Typehint, optional
str_list: List[str] = [1, 2, 3]

empty_list.append(1)                # [1]
1 in empty_list                     # = True
2 not in empty_list                 # = True
empty_list.remove(1)                # []
empty_list + [1, 2]                 # [1, 2]
sorted([2, 5, 1, 4])                # [1, 2, 4, 5]


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
new_dict = dict()                   # Alternative initialization
a_dict: Dict[Any, Any] = {}         # Typehint, optional
str_int_dict: Dict[str, int] = {}

simple_dict["key3"]= 3
"key3" in simple_dict               # = True
simple_dict["key3"]                 # = 3


# Sets (set)
empty_set = set()                   # NOTE: Just {} is a dict
simple_set = { 1, 2, 3, 4 }
mixed_set = { 1, '2', 3, '4' }
a_set: Set[Any] = set()
int_set: Set[int] = { 1, 2, 3, 4 }

simple_set.add(5)                   # { 1, 2, 3, 4, 5 }
5 in empty_set                      # = True
simple_set.remove(5)                # { 1, 2, 3, 4 }
simple_set.union({ 5 })             # { 1, 2, 3, 4, 5 }
simple_set.intersection({ 1, 2 })   # { 1, 2 }


# Branching
if False:
    print("if")
elif False:
    print("elif instead of else if")
else:
    print("else")

that = False
var = "this" if not that else "that"


# Looping
i = 0
while i < 10:
    i += 1

nums = [1, 2, 3, 4]
for num in nums:
    print(num)

for i in range(10):
    print(i)


# Files
read_file = open("onepager.py", "r")
contents = read_file.read()
print(f"Num chars: {len(contents)}")
read_file.close()

with open("onepager.py", "r") as context_manager_file:
    lines = context_manager_file.readlines()
    print(f"Num lines: {len(lines)}")


# Functions
def example_function():
    pass


# Classes
class Example:
    def __init__(self, constructor_arg1: str):
        self.member_var1 = constructor_arg1

    def __str__(self) -> str:
        """Convert an instance of Example to a string"""
        return f"{self.member_var1}"

example = Example("var")
print(str(example))
type(example) == Example


# Data Classes
@dataclass
class DataClass:
    member1: int
    member2: float
    member3: str

ds = DataClass(1, 2.0, "3")
type(ds) == DataClass
