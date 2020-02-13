"""
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 2^0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2^4 = 16
Example 3:

Input: 218
Output: false
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        two_list = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

        c = 9

        while n != 1:
            if n >= two_list[c]:
                n, m = divmod(n, two_list[c])
                if m != 0:
                    return False
            else:
                c -= 1
                if c < 0:
                    return False

        return True


s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(218))

"""
Runtime: 24 ms, faster than 93.61% of Python3 online submissions for Power of Two.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Power of Two.

https://ko.wikipedia.org/wiki/2%EC%9D%98_%EA%B1%B0%EB%93%AD%EC%A0%9C%EA%B3%B1
"""