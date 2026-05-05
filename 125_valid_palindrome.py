"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy
Topic: Two Pointers, String
"""

# Approach 1 — Clean then reverse
# Time: O(n) | Space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]


# Approach 2 — Clean then two pointers
# Time: O(n) | Space: O(n)
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
