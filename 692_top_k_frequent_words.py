"""
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/
Difficulty: Medium
Topic: Hash Map, Sorting
"""

from typing import List
from collections import Counter

# Time: O(n log n) | Space: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return sorted(freq.keys(), key=lambda x: (-freq[x], x))[:k]
                                              # First element in tuple (-freq[x]) → Sort by frequency descending
                                              # Second element (x) → Break ties by alphabetical order
