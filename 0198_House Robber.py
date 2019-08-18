"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


class Solution(object):
    def __init__(self):
        self.nums = []
        self.max_money = 0
        self.step_max_money = []

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        self.step_max_money = [0] * len(nums)

        for i in [0, 1]:
            self.cal_rob_money(i, 0)

        return self.max_money

    def cal_rob_money(self, num, get_money):
        if num >= len(self.nums):
            self.max_money = get_money if get_money > self.max_money else self.max_money
            return None

        get_money = self.nums[num] + get_money
        if get_money > self.step_max_money[num]:
            self.step_max_money[num] = get_money
        else:
            return None

        for i in [2, 3]:
            self.cal_rob_money(num + i, get_money)


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))

"""
Runtime: 28 ms, faster than 6.99% of Python online submissions for House Robber.
Memory Usage: 11.8 MB, less than 29.79% of Python online submissions for House Robber.
"""
