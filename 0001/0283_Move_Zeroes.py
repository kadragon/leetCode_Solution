"""
https://leetcode.com/problems/move-zeroes/
"""


class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_count] = nums[i]
                non_zero_count += 1

        for i in range(non_zero_count, len(nums)):
            nums[i] = 0


s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])

"""
Runtime: 48 ms, faster than 75.04% of Python3 online submissions for Move Zeroes.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Move Zeroes.
"""