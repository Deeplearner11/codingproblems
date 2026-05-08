"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy
Topic: Array, Sliding Window

You are given an array prices where prices[i] is the price of a given
stock on the ith day. You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the future
to sell that stock. Return the maximum profit you can achieve from this
transaction. If you cannot achieve any profit, return 0.

Input:  prices = [7,1,5,3,6,4]
Output: 5  (buy at 1, sell at 6)

Input:  prices = [7,6,4,3,1]
Output: 0  (prices only decrease, no profit possible)
"""

from typing import List

# INTUITION
# track the minimum price seen so far as we walk through.
# at each day, calculate profit if we sold today (price - min_price).
# update max profit if current profit is better.
# we never sell before we buy because min_price is always from a previous day.
#
# trace on [7,1,5,3,6,4]:
# price=7  min=7  profit=0    max_profit=0
# price=1  min=1  profit=0    max_profit=0
# price=5  min=1  profit=4    max_profit=4
# price=3  min=1  profit=2    max_profit=4
# price=6  min=1  profit=5    max_profit=5
# price=4  min=1  profit=3    max_profit=5
# result = 5 ✓

# PATTERN — track running minimum + running best outcome
# any time a problem asks for best/max result between two days,
# two indices, or two elements where order matters (must come before),
# track the best "left side" seen so far and compute the result at each step.
# same pattern appears in: trapping rain water, best profit with cooldown.

# Time: O(n) | Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
