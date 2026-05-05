"""
Fundamentals: Counter + Heap Patterns
Topic: Collections, heapq
"""

# -------------------------------------------------------
# COUNTER
# -------------------------------------------------------
# Counter takes any iterable and counts how many times
# each element appears. Returns a dict-like object.

from collections import Counter

# on a list
nums = [1, 1, 2, 3, 3, 3]
freq = Counter(nums)
print(freq)           # Counter({3: 3, 1: 2, 2: 1})
print(freq[3])        # 3  — how many times 3 appears
print(freq[99])       # 0  — missing keys return 0, no KeyError

# on a string (counts characters)
freq = Counter("aabbbc")
print(freq)           # Counter({'b': 3, 'a': 2, 'c': 1})

# on a sentence (split into words first)
freq = Counter("the cat sat on the mat the cat".split())
print(freq)           # Counter({'the': 3, 'cat': 2, 'sat': 1, ...})

# most_common(k) — returns top k as list of (element, count) tuples
print(freq.most_common(2))   # [('the', 3), ('cat', 2)]


# -------------------------------------------------------
# HEAP PATTERNS
# -------------------------------------------------------

import heapq

# ---- PATTERN 1: Always get min fast ----
# Use a min-heap. Smallest element always sits at index 0.
# heappop always returns the smallest.

nums = [5, 2, 8, 1, 9]
heapq.heapify(nums)

print(heapq.heappop(nums))   # 1  — smallest
print(heapq.heappop(nums))   # 2
print(heapq.heappop(nums))   # 5


# ---- PATTERN 2: Always get max fast ----
# Python has no built-in max-heap.
# Trick: negate all values. Push negatives, pop negatives, negate back.

nums = [5, 2, 8, 1, 9]
max_heap = [-n for n in nums]
heapq.heapify(max_heap)

print(-heapq.heappop(max_heap))   # 9  — largest
print(-heapq.heappop(max_heap))   # 8
print(-heapq.heappop(max_heap))   # 5


# ---- PATTERN 3: Top K Largest ----
# Use a min-heap of size k.
# Keep a "top k club" — when club exceeds k, kick the smallest out.
# At the end, the k largest remain.
#
# Why min-heap? Because you want to kick out the smallest
# of your current top-k candidates, and min-heap always
# has the smallest sitting right at the front ready to pop.
#
# nums = [5, 2, 8, 1, 9, 3, 7],  k = 3
#
# push 5 → [5]
# push 2 → [2, 5]
# push 8 → [2, 5, 8]
# push 1 → [1, 5, 8, 2]  len > 3 → pop 1  → [2, 5, 8]
# push 9 → [2, 5, 8, 9]  len > 3 → pop 2  → [5, 9, 8]
# push 3 → [3, 9, 8, 5]  len > 3 → pop 3  → [5, 9, 8]
# push 7 → [5, 9, 8, 7]  len > 3 → pop 5  → [7, 9, 8]
#
# final heap = [7, 8, 9] → top 3 largest ✓

def top_k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)       # kick out the smallest
    return sorted(heap, reverse=True)

print(top_k_largest([5, 2, 8, 1, 9, 3, 7], 3))   # [9, 8, 7]


# ---- PATTERN 4: Top K Smallest ----
# Use a max-heap of size k.
# When club exceeds k, kick the largest out.
# At the end, the k smallest remain.
#
# Same logic but flipped — negate values to simulate max-heap.
#
# nums = [5, 2, 8, 1, 9, 3, 7],  k = 3
#
# push -5 → [-5]
# push -2 → [-5, -2]
# push -8 → [-8, -2, -5]
# push -1 → [-8, -2, -5, -1]  len > 3 → pop -8 (i.e. kick 8) → [-5, -2, -1]
# push -9 → [-9, -2, -1, -5]  len > 3 → pop -9 (i.e. kick 9) → [-5, -2, -1]
# push -3 → [-5, -2, -1, -3]  len > 3 → pop -5 (i.e. kick 5) → [-3, -2, -1]
# push -7 → [-7, -2, -1, -3]  len > 3 → pop -7 (i.e. kick 7) → [-3, -2, -1]
#
# final heap = [-3, -2, -1] → negate → [3, 2, 1] → top 3 smallest ✓

def top_k_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)    # negate to simulate max-heap
        if len(heap) > k:
            heapq.heappop(heap)       # kick out the largest (most negative)
    return sorted(-n for n in heap)

print(top_k_smallest([5, 2, 8, 1, 9, 3, 7], 3))   # [1, 2, 3]


# -------------------------------------------------------
# SUMMARY
# -------------------------------------------------------
#
#   Goal                  Heap type         Kick out when > k
#   ----                  ---------         -----------------
#   Top K largest         min-heap          smallest  (heappop directly)
#   Top K smallest        max-heap          largest   (negate values)
#   Always get min fast   min-heap          —
#   Always get max fast   max-heap          —         (negate values)
