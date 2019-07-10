"""
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1].

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        flag = 1

        if x < 0:
            flag = 0
            x *= -1

        conv = int(str(x)[::-1])
        if flag == 0:
            conv *= -1

        if (-2 ** 31 > conv) or (2 ** 31 - 1 < conv):
            return 0

        return conv

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(1534236469))
print(-2 ** 31)

