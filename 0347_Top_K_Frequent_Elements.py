"""
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import operator


def count_element(nums: [int]) -> [int]:
    count_dict = {}
    for i in nums:
        try:
            count_dict[i] += 1
        except KeyError:
            count_dict[i] = 1

    return count_dict


class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        c_dict = count_element(nums)
        sorted_c_dict = sorted(c_dict.items(), key=operator.itemgetter(1), reverse=True)

        ans = []

        for key, _ in list(sorted_c_dict)[0:k]:
            ans.append(key)

        return ans


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(s.topKFrequent([1], 1))

"""
Runtime: 104 ms, faster than 96.37% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.1 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
"""
