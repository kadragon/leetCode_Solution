"""
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            i = m + n - 1

            if nums1[m-1] > nums2[n-1] and m-1 > -1:
                nums1[i] = nums1[m-1]
                m -= 1
                print('<')
            else:
                nums1[i] = nums2[n-1]
                n -= 1
                print(">")

        print(nums1)

    def merge2(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        nums1 = sorted(nums1[:m] + nums2[:n])


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
s.merge([2, 0], 1, [1], 1)

"""
Runtime: 36 ms, faster than 57.75% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Sorted Array.
"""
