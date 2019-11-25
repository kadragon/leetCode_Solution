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


class Solution:
    def __init__(self):
        self.end_flag = False
        self.answer = ''
        self.count = 0

    def strWithout3a3b(self, A: int, B: int) -> str:
        self.answer_maker('', A, B)
        return self.answer

    def answer_maker(self, s: str, a, b):
        if self.end_flag:
            return None

        self.count += 1

        if a == 0 and b == 0:
            self.answer = s
            self.end_flag = True
            return None

        if a > 1 and s[-1:] != 'a':
            self.answer_maker(s + 'aa', a - 2, b)
        if b > 1 and s[-1:] != 'b':
            self.answer_maker(s + 'bb', a, b - 2)

        if a != 0 and s[-2:] != 'aa':
            self.answer_maker(s + 'a', a - 1, b)
        if b != 0 and s[-2:] != 'bb':
            self.answer_maker(s + 'b', a, b - 1)

        return None


s = Solution()
print(s.strWithout3a3b(1, 1))

s = Solution()
print(s.strWithout3a3b(1, 2))

s = Solution()
print(s.strWithout3a3b(4, 1))

s = Solution()
print(s.strWithout3a3b(5, 2))

s = Solution()
print(s.strWithout3a3b(3, 8))

s = Solution()
print(s.strWithout3a3b(27, 33))

s = Solution()
print(s.strWithout3a3b(71, 81))

s = Solution()
print(s.strWithout3a3b(82, 100))
