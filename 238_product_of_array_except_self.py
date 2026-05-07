"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium
Topic: Array, Prefix Product

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all elements except nums[i].
You must solve it without division in O(n) time.

Input:  nums = [1,2,3,4]
Output: [24,12,8,6]

Input:  nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List

# INTUITION
# for each index i, the answer is:
#   (product of everything to the LEFT of i) * (product of everything to the RIGHT of i)
#
# pass 1 left → right: fill answer[i] with product of all elements left of i
# pass 2 right → left: multiply answer[i] by product of all elements right of i
#
# trace on [1,2,3,4]:
#
# pass 1 (left products):
# i=0  answer[0]=1          left=1*1=1
# i=1  answer[1]=1          left=1*2=2
# i=2  answer[2]=2          left=2*3=6
# i=3  answer[3]=6          left=6*4=24
# answer = [1, 1, 2, 6]
#
# pass 2 (multiply right products):
# i=3  answer[3]=6*1=6      right=1*4=4
# i=2  answer[2]=2*4=8      right=4*3=12
# i=1  answer[1]=1*12=12    right=12*2=24
# i=0  answer[0]=1*24=24    right=24*1=24
# answer = [24, 12, 8, 6] ✓

# Time: O(n) | Space: O(1)  (output array doesn't count as extra space)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left_product = 1
        right_product = 1

        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
