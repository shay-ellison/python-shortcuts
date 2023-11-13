"""
*lists*

Things you can do with Python 3 lists. For rundown on list basics,
see basics.py.

You can import this file into Python or run it with python.
python lists.py
"""

# A Python list is like an array list in other languages
alist = [3, 4, 1, 5, 6, 2]

# We often want to sort lists, of course.
# `sorted` creates a new list in sorted order, ascending
alist_sorted_asc = sorted(alist)
print(alist_sorted_asc)								# [1, 2, 3, 4, 5, 6]

# The original list is unmodified
print(alist)										# [3, 4, 1, 5, 6, 2]

# We can sort in descending order as well
alist_sorted_desc = sorted(alist, reverse=True)
print(alist_sorted_desc)							# [6, 5, 4, 3, 2, 1]

# Many types are sorted lexigraphically (by checking from left-to-right)

# strings for instance
sorted_strings = sorted(["bbstr", "aastr", "abstr"])
print(sorted_strings)								# ['aastr', 'abstr', 'bbstr']

# tuples as well
sorted_tuples = sorted([(2, 1), (1, 1), (1, 2)])
print(sorted_tuples)								# [(1, 1), (1, 2), (2, 1)]


# Building lists
# We can start by just appending elements we want
numbers = []
for num in range(1, 10):
	numbers.append(num)
print(numbers)										# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# We can simplify this by using *list comprehensions*
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
numbers = [num for num in range(1, 10)]
print(numbers)										# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List comprehensions can scale to bigger tasks
# We might use a loop like this to get even numbers
even_numbers = []
for num in range(1, 10):
	if num % 2 == 0:
		even_numbers.append(num)
print(even_numbers)									# [2, 4, 6, 8]

# But again this can be written with list comprehension
# By adding the inner if statement to the end of the comprehension statement
even_numbers = [num for num in range(1, 10) if num % 2 == 0]
print(even_numbers)									# [2, 4, 6, 8]

# We can do this with another loop as well
pairs = []
for x in range(2):
	for y in range(2):
		pair = (x, y)
		pairs.append(pair)
print(pairs)										# [(0, 0), (0, 1), (1, 0), (1, 1)]

# In list comprehension form
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)										# [(0, 0), (0, 1), (1, 0), (1, 1)]

# We can add 0 or more for and if statements after the first for
# Think of each addition as being nested under the previous statement
# For example,
pairs_with_even = []
for x in range(2):
	for y in range(1, 5):
		if y % 2 == 0:
			pair = (x, y)
			pairs_with_even.append(pair)
print(pairs_with_even)								# [(0, 2), (0, 4), (1, 2), (1, 4)]

# Can be written by flattening the nested statements
pairs_with_even = [(x, y) for x in range(2) for y in range(1, 5) if y % 2 == 0]
print(pairs_with_even)								# [(0, 2), (0, 4), (1, 2), (1, 4)]
