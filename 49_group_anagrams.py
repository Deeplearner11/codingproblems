"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Topic: Array, Hash Map, String

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from typing import List

# Approach 1 — Sort as key
# signature: sort each word → anagrams produce the same sorted string
# Time: O(n * k log k) | Space: O(n)  where k = max word length
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]
        return list(dic.values())


# -------------------------------------------------------
# HASHING
# -------------------------------------------------------
# hashing = finding a signature for something so you can
# jump to it instantly instead of scanning.
#
# two words are anagrams if they have the exact same
# character counts. so the signature is a tuple of 26
# counts — one per letter a-z.
#
# "eat" → a=1, e=1, t=1, rest=0 → (1,0,0,0,1,0,...,1,...)
# "tea" → a=1, e=1, t=1, rest=0 → (1,0,0,0,1,0,...,1,...)
# same signature → same group
#
# ord(c) - ord('a') converts letter to index → 'a'=0, 'b'=1 ... 'z'=25
# tuple(count) because lists cant be dict keys, tuples can.
# this avoids sorting → O(k) per word instead of O(k log k)


# Approach 2 — Character count as key (no libraries)
# Time: O(n * k) | Space: O(n)
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]
        return list(dic.values())
