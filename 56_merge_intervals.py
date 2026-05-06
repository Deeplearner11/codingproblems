"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
Difficulty: Medium
Topic: Array, Sorting

Given an array of intervals, merge all overlapping intervals
and return an array of the non-overlapping intervals.

Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input:  intervals = [[1,4],[4,5]]
Output: [[1,5]]
"""

from typing import List

# INTUITION
# sort by start time so we only ever need to compare with the previous interval.
# if current start <= prev end → overlap → extend prev end to max of both ends.
# if no overlap → save prev, move to current.
# always append prev after the loop — last interval never gets added inside it.

# Time: O(n log n) | Space: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])
            else:
                answer.append(prev)
                prev = intervals[i]

        answer.append(prev)
        return answer
