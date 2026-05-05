"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
Difficulty: Easy
Topic: Array, Two Pointers
"""

from typing import List

# Approach 1 — Count and shift
# Time: O(n) | Space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i - count] = nums[i]
        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0


# Approach 2 — Two pointers
# left tracks where next non-zero should go.
# every time right finds a non-zero, swap it to left.
# zeroes naturally bubble to the end.
# Time: O(n) | Space: O(1)
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
