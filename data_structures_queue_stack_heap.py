"""
Data Structures: Queue, Stack, and Heap
Fundamentals — no Leetcode number
Topic: Linear Data Structures
"""

# -------------------------------------------------------
# QUEUE — First In, First Out (FIFO)
# -------------------------------------------------------
# Like a line at a shop. First person in, first person out.
# Order of insertion is what matters.
#
# Use collections.deque (not a list) — O(1) on both ends.

from collections import deque

queue = deque()
queue.append(5)     # push to back  → [5]
queue.append(2)     # push to back  → [5, 2]
queue.append(8)     # push to back  → [5, 2, 8]

queue.popleft()     # pop from front → returns 5  (first in, first out)
queue.popleft()     # → returns 2
queue.popleft()     # → returns 8


# -------------------------------------------------------
# STACK — Last In, First Out (LIFO)
# -------------------------------------------------------
# Like a stack of plates. Last plate placed is first removed.
# A plain Python list works perfectly as a stack.

stack = []
stack.append(5)     # push  → [5]
stack.append(2)     # push  → [5, 2]
stack.append(8)     # push  → [5, 2, 8]

stack.pop()         # pop from top → returns 8  (last in, first out)
stack.pop()         # → returns 2
stack.pop()         # → returns 5


# -------------------------------------------------------
# HEAP — Smallest Out First (Priority)
# -------------------------------------------------------
# Doesn't care about insertion order at all.
# The smallest element always comes out first.
# Think: hospital ER — most critical patient seen first,
# regardless of when they arrived.
#
# Python's heapq is a MIN-heap by default.
# Three operations: heappush, heappop, heapify

import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)

heapq.heappop(heap)     # → returns 2  (smallest, even though it wasn't first)
heapq.heappop(heap)     # → returns 5
heapq.heappop(heap)     # → returns 8

# heapify: turn an existing list into a heap in-place
nums = [5, 2, 8, 1, 9]
heapq.heapify(nums)
print(nums[0])          # → 1  (smallest is always at index 0)

# MAX-HEAP trick: negate values (Python has no built-in max-heap)
max_heap = [-n for n in [5, 2, 8, 1, 9]]
heapq.heapify(max_heap)
print(-heapq.heappop(max_heap))   # → 9  (largest)


# -------------------------------------------------------
# SUMMARY
# -------------------------------------------------------
#
#   Structure   Order           Pop returns      Python
#   ---------   -----           -----------      ------
#   Queue       FIFO            first inserted   collections.deque
#   Stack       LIFO            last inserted    list
#   Heap        Priority        smallest value   heapq
