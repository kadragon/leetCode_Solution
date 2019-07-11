"""
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

Given an array A of non-negative integers,
return the maximum sum of elements in two non-overlapping (contiguous) subarrays,
which have lengths L and M.  (For clarification,
the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which
V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.


Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.


Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.


Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.


Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""


class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        l_sum = [0] * (len(A) + max([L, M]))
        m_sum = [0] * (len(A) + max([L, M]))

        for x in range(len(A)):
            for l_count in range(L):
                l_sum[x+l_count] += A[x]
            for m_count in range(M):
                m_sum[x + m_count] += A[x]

        l_sum = l_sum[L-1:-L]
        m_sum = m_sum[M-1:-M]

        max_sum = 0

        for x in range(len(l_sum)):
            sub_m_sum = (m_sum[0:x-M+1] if (x-M+1) > 0 else []) + m_sum[x+L+1:]
            if len(sub_m_sum) == 0:
                continue

            if l_sum[x] + max((m_sum[0:x-M+1] if (x-M+1) > 0 else []) + m_sum[x+L+1:]) > max_sum:
                max_sum = l_sum[x] + max((m_sum[0:x-M+1] if (x-M+1) > 0 else []) + m_sum[x+L+1:])

        return max_sum


s = Solution()
result = s.maxSumTwoNoOverlap([0, 6, 5, 2, 2, 5, 1, 9, 4], L=1, M=2)
print(result)

result = s.maxSumTwoNoOverlap([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2)
print(result)

result = s.maxSumTwoNoOverlap([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], L=4, M=3)
print(result)

result = s.maxSumTwoNoOverlap([1, 0, 1], L=1, M=1)
print(result)
