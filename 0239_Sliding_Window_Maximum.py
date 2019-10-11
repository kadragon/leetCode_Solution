"""
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums,
there is a sliding window of size k
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        ans = []
        if nums_len == 0 or k == 0:
            return []

        for i in range(nums_len - k + 1):
            ans.append(max(nums[i:i + k]))

        return ans


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))

"""
Runtime: 712 ms, faster than 11.61% of Python online submissions for Sliding Window Maximum.
Memory Usage: 18.8 MB, less than 62.07% of Python online submissions for Sliding Window Maximum.
"""
