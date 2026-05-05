"""
344. Reverse String
https://leetcode.com/problems/reverse-string/
Difficulty: Easy
Topic: Two Pointers, String
"""

# -------------------------------------------------------
# INTUITION
# -------------------------------------------------------
# We need to reverse the list IN PLACE — the function returns
# None, meaning we cannot return a new list. We must mutate
# the original object directly.
#
# Key gotcha: s = s[::-1] does NOT work because it only
# rebinds the local variable s to a new list. The original
# list the caller passed in stays unchanged.
# s[:] = s[::-1] works because slice assignment mutates the
# contents of the original object in place.
#
# Optimal approach: two pointers from both ends, swap and
# move inward. O(1) space, no extra list created.

# -------------------------------------------------------
# APPROACH 1 — Slice assignment (Pythonic, O(n) space)
# -------------------------------------------------------
# Time: O(n) | Space: O(n)

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


# -------------------------------------------------------
# APPROACH 2 — Two Pointers (optimal, O(1) space)
# -------------------------------------------------------
# Time: O(n) | Space: O(1)
#
# left=0, right=4  →  swap  →  ["o","e","l","l","h"]
# left=1, right=3  →  swap  →  ["o","l","l","e","h"]
# left=2, right=2  →  stop

class Solution2:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# -------------------------------------------------------
# TESTS
# -------------------------------------------------------
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    Solution2().reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    Solution2().reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]

    print("All tests passed.")
