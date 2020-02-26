"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        max_value, sub_value = nums[0], nums[0]

        for i in nums[1:]:
            sub_value = max(sub_value+i, i)
            max_value = max(sub_value, max_value)

        return max_value

s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


"""
Runtime: 56 ms, faster than 98.81% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.5 MB, less than 87.80% of Python3 online submissions for Maximum Subarray.
"""