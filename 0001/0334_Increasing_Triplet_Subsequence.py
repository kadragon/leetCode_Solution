"""
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""


class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        inc_list = [None] * 3

        for i in nums:
            for j in range(3):
                if inc_list[j] is None or inc_list[j] > i:
                    inc_list[j] = i
                    if j == 2:
                        return True
                    break

                if inc_list[j] < i:
                    continue

                if inc_list[j] == i:
                    break

        return False


s = Solution()
print(s.increasingTriplet([1, 2, 3, 4, 5]))
print(s.increasingTriplet([5, 4, 3, 2, 1]))

"""
Runtime: 64 ms, faster than 23.76% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 13.3 MB, less than 88.89% of Python3 online submissions for Increasing Triplet Subsequence.

https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
"""