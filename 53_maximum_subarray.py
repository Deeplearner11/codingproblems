"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium
Topic: Array, Dynamic Programming

Given an integer array nums, find the subarray with the
largest sum and return its sum.

Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6  ([4,-1,2,1])

Input:  nums = [1]
Output: 1

Input:  nums = [5,4,-1,7,8]
Output: 23
"""

from typing import List

# KADANE'S ALGORITHM
# at every index ask one question:
# is it better to extend the previous subarray, or start fresh here?
#
# max_current = max(nums[i], max_current + nums[i])
#
# if max_current + nums[i] < nums[i] → previous subarray is dragging us down
# → drop it and start fresh at nums[i]
# if max_current + nums[i] >= nums[i] → extending is better → keep going
#
# max_global tracks the best we've seen across all positions.
# start both at nums[0] not 0 — array could be all negative.
#
# trace on [-2,1,-3,4,-1,2,1,-5,4]:
# i=1  num=1   max_current = max(1,  -2+1) = max(1, -1)  = 1   max_global=1
# i=2  num=-3  max_current = max(-3, 1-3)  = max(-3,-2)  = -2  max_global=1
# i=3  num=4   max_current = max(4,  -2+4) = max(4, 2)   = 4   max_global=4
# i=4  num=-1  max_current = max(-1, 4-1)  = max(-1, 3)  = 3   max_global=4
# i=5  num=2   max_current = max(2,  3+2)  = max(2, 5)   = 5   max_global=5
# i=6  num=1   max_current = max(1,  5+1)  = max(1, 6)   = 6   max_global=6
# i=7  num=-5  max_current = max(-5, 6-5)  = max(-5, 1)  = 1   max_global=6
# i=8  num=4   max_current = max(4,  1+4)  = max(4, 5)   = 5   max_global=6
# result = 6 ✓

# Time: O(n) | Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_current = max_global = nums[0]

        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current

        return max_global
