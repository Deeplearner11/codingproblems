"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium
Topic: Array, Two Pointers, Greedy

You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]). Find two lines that together with the x-axis form a
container, such that the container contains the most water. Return the
maximum amount of water a container can store.

Input:  height = [1,8,6,2,5,4,8,3,7]
Output: 49  (lines at index 1 and 8, min(8,7)*7 = 49)

Input:  height = [1,1]
Output: 1
"""

from typing import List

# INTUITION
# area = min(height[left], height[right]) * (right - left)
# start with widest container (left=0, right=n-1).
# to possibly find a larger area we must increase the height,
# so move the pointer with the smaller height inward.
# moving the taller side inward can only make things worse —
# width decreases and height is still bounded by the shorter side.
#
# trace on [1,8,6,2,5,4,8,3,7]:
# l=0,r=8  area=min(1,7)*8=8    move left  (height[0]=1 < height[8]=7)
# l=1,r=8  area=min(8,7)*7=49   move right (height[8]=7 < height[1]=8)
# l=1,r=7  area=min(8,3)*6=18   move right
# l=1,r=6  area=min(8,8)*5=40   move right (equal, move either)
# ...
# max_area = 49 ✓

# PATTERN — two pointers shrinking inward
# when brute force is O(n²) trying all pairs,
# use two pointers from both ends and greedily eliminate
# the side that cannot possibly give a better answer.
# same pattern: trapping rain water, 3Sum.

# Time: O(n) | Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
