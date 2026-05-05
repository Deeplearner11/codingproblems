"""
Fundamentals: Lambda Functions
Topic: Python Basics
"""

# a lambda is just a function without a name
# lambda argument : what_to_return

# these two are identical
def square(x):
    return x * 2

square = lambda x: x * 2


# -------------------------------------------------------
# PATTERNS
# -------------------------------------------------------

# sort descending
nums = [3, 1, 4, 1, 5, 9]
sorted(nums, key=lambda x: -x)                    # [9, 5, 4, 3, 1, 1]

# sort by second element of tuple
pairs = [(1, 3), (2, 1), (3, 2)]
sorted(pairs, key=lambda x: x[1])                 # [(2,1), (3,2), (1,3)]

# sort by length
words = ["banana", "apple", "cherry"]
sorted(words, key=lambda x: len(x))               # ["apple", "banana", "cherry"]

# sort by length, then alphabetically for ties
words = ["cat", "dog", "at", "be"]
sorted(words, key=lambda x: (len(x), x))          # ["at", "be", "cat", "dog"]

# sort by frequency descending, then alphabetically for ties  ← used in 692
from collections import Counter
freq = Counter(["the", "cat", "the", "dog", "the", "cat"])
sorted(freq.keys(), key=lambda x: (-freq[x], x))  # ["the", "cat", "dog"]
