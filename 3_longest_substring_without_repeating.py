"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: Medium
Topic: String, Sliding Window, Hash Set

Given a string s, find the length of the longest substring
without repeating characters.

Input:  s = "abcabcbb"
Output: 3  ("abc")

Input:  s = "bbbbb"
Output: 1  ("b")
"""

# INTUITION
# sliding window with two pointers left and right.
# expand right to grow the window, shrink from left when duplicate found.
# char_set tracks what's currently inside the window.
# window size at any point = right - left + 1

# Time: O(n) | Space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length
