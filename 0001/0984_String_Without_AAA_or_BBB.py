"""
https://leetcode.com/problems/string-without-aaa-or-bbb/

Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.


Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"


Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""
from math import ceil


class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A == 0:
            return 'b' * B
        if B == 0:
            return 'a' * A

        value_list = [A, B, 'a', 'b'] if A < B else [B, A, 'b', 'a']
        mod_value = ceil(value_list[1] / (value_list[0] + 1))
        d_mod = value_list[1] // mod_value
        mod_d_value = value_list[0] - d_mod

        # print(value_list, mod_value, d_mod, mod_d_value)

        ans = ''
        while value_list[0] > 0 or value_list[1] > 0:
            if value_list[1] > 0:
                if value_list[1] >= mod_value:
                    ans += value_list[3] * mod_value
                    value_list[1] -= mod_value
                else:
                    ans += value_list[3] * value_list[1]
                    value_list[1] = 0
            if value_list[0] > 0:
                ans += value_list[2]
                value_list[0] -= 1

                if mod_d_value > 0:
                    ans += value_list[2]
                    mod_d_value -= 1
                    value_list[0] -= 1

        return ans


s = Solution()
print(s.strWithout3a3b(1, 1))
print(s.strWithout3a3b(1, 2))
print(s.strWithout3a3b(4, 1))
print(s.strWithout3a3b(5, 2))
print(s.strWithout3a3b(3, 8))
print(s.strWithout3a3b(27, 33))
print(s.strWithout3a3b(71, 81))

"""
Runtime: 28 ms, faster than 93.55% of Python3 online submissions for String Without AAA or BBB.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for String Without AAA or BBB.
"""
