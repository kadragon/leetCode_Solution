"""
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        pow_list = [1.0]
        pow_count = [1]

        if n < 0:
            x = 1/x
            n *= -1

        answer = 1.0

        if n == 1:
            return x

        for i in range(31):
            if i == 0:
                pow_list[i] = x
            else:
                if pow(2, i) < n:
                    pow_list.append(pow_list[-1]*pow_list[-1])
                    pow_count.append(pow_count[-1]*2)
                else:
                    break

        i = len(pow_list) - 1

        while n > 0:
            if n >= pow_count[i]:
                answer *= pow_list[i]
                n -= pow_count[i]
            else:
                i -= 1

        return answer


s = Solution()
print(s.myPow(2.00000, 10))
print(s.myPow(2.10000, 3))
print(s.myPow(2.00000, -2))


"""
Runtime: 32 ms, faster than 32.88% of Python3 online submissions for Pow(x, n).
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
"""
