"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) < 2:
            return 0

        sub_max, ans_max, min_i = 0, 0, 0

        for i in range(1, len(prices)):
            if prices[i] < prices[min_i]:
                sub_max = 0
                min_i = i
                continue
            if prices[i] - prices[min_i] > sub_max:
                sub_max = prices[i] - prices[min_i]
                ans_max = max(ans_max, sub_max)

        return ans_max


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))

"""
Runtime: 56 ms, faster than 94.91% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""
