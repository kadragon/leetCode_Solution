"""
https://leetcode.com/problems/counting-bits/

Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate
the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?

Space complexity should be O(n).

Can you do it like a boss?
Do it without using any builtin function like __builtin_popcount
in c++ or in any other language.
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bit_count = [0] * (num + 1)
        div_list = []

        k = 1
        while 2 ** k <= num:
            div_list.append(2 ** k)
            k += 1

        j = 0
        for i in range(1, num + 1):
            ins = 0
            for div in div_list:
                if i % div == 0:
                    ins -= 1
                else:
                    break
            j = j + ins + 1
            bit_count[i] = j

        return bit_count


s = Solution()
print(s.countBits(2))
print(s.countBits(4))
print(s.countBits(5))
print(s.countBits(20))

"""
Runtime: 80 ms, faster than 37.47% of Python online submissions for Counting Bits.
Memory Usage: 15.8 MB, less than 27.27% of Python online submissions for Counting Bits.
"""
