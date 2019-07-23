"""
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.


Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 리스트의 최대 길이 계산
        nums_len = len(nums)

        # 특정 시점에서 도달 가능한 최대 위치
        max_attach = 0

        # 모든 리스트 값을 하나씩 확인하여, 그 리스트에서 도달 할 수 있는 최대 길이 추정
        for i in range(nums_len):
            # 단, 도달 가능한 최대 위치 보다 index 위치가 같거나 작아야 함.
            if max_attach >= i:
                # 도달 최대치 계산
                tmp_max = i+nums[i]
                max_attach = max(tmp_max, max_attach)
            else:
                # index 위치를 더 이상 도달 할 수 없으므로, 포기
                break

        # 도달 가능 범위가 최대 길이보다 넓다면 True, 아니면 False
        return True if max_attach >= nums_len-1 else False


s = Solution()

result = s.canJump([2, 3, 1, 1, 4])
print(result)

result = s.canJump([3, 2, 1, 0, 4])
print(result)

result = s.canJump([2, 0])
print(result)

result = s.canJump([2, 5, 0, 0])
print(result)

result = s.canJump([0])
print(result)

result = s.canJump([0, 2, 3])
print(result)
