"""
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        check_list = []

        front = "([{"
        end = ")]}"
        for c in s:
            if c in front:
                check_list.append(c)
            else:
                try:
                    if front.find(check_list[-1]) == end.find(c):
                        check_list = check_list[:-1]
                    else:
                        return False
                except KeyError:
                    return False

        return True if len(check_list) == 0 else False


s = Solution()
print(s.isValid("()"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("()[]"))
print(s.isValid("{()}"))

"""
Runtime: 48 ms, faster than 8.23% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.

Hint: https://leetcode.com/problems/valid-parentheses/discuss/9482/8-line-Python-solution-stack-40ms
"""