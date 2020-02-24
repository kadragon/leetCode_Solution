"""
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1

        return c


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

"""
Runtime: 24 ms, faster than 95.78% of Python3 online submissions for Remove Element.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Remove Element.
"""