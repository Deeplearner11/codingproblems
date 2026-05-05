"""
1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy
Topic: Array, Hash Map
"""

from typing import List

# INTUITION
# for each num, check if (target - num) already exists in the dict.
# if yes, we found our pair. if no, store num and its index.

# Time: O(n) | Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            if (target - num) in dic:
                return [i, dic[target - num]]
            dic[num] = i
