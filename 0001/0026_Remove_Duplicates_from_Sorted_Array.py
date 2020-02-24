"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        count = 0
        for i in range(len(nums)):
            try:
                if i == 0 or nums[i] != nums[i-1]:
                    nums[count] = nums[i]
                    count += 1
            except IndexError:
                break

        return count


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(s.removeDuplicates([1]))

"""
Runtime: 84 ms, faster than 76.95% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.5 MB, less than 95.90% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
