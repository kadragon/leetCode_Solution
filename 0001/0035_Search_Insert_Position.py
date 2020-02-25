"""
https://leetcode.com/problems/search-insert-position/
"""


class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < target:
                return i + 1

        return 0


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))

"""
Runtime: 44 ms, faster than 92.04% of Python3 online submissions for Search Insert Position.
Memory Usage: 13.6 MB, less than 91.04% of Python3 online submissions for Search Insert Position.
"""
