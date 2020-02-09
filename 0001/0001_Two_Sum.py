"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums: [], target: int) -> [int, int]:
        for x in range(len(nums)):
            if target-nums[x] in nums:
                y = nums.index(target-nums[x])
                if x != y:
                    return [x, nums.index(target-nums[x])]


s = Solution()
print(s.twoSum([1, 2, 3], 4))
