"""
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/
Difficulty: Medium
Topic: Array, Hash Map
"""

from typing import List

# INTUITION
# all numbers are in range [1, n] so every number x can map to index x-1.
# when we visit x, negate nums[x-1] to mark "x has been seen".
# if nums[x-1] is already negative when we visit x again → x is a duplicate.
# abs(x) is needed because the number at current index may already be negated.
# this avoids using a hash set → O(1) space.
# pattern: index as hash — only works when values are guaranteed in [1, n].

# Time: O(n) | Space: O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            x = abs(x)
            if nums[x - 1] < 0:
                ans.append(x)
            nums[x - 1] *= -1
        return ans
