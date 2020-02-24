"""
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len, nee_len = len(haystack), len(needle)

        if nee_len == 0:
            return 0

        for i in range(hay_len - nee_len + 1):
            if haystack[i:i + nee_len] == needle:
                return i

        return -1


s = Solution()
print(s.strStr(haystack="hello", needle="ll"))
print(s.strStr(haystack="aaaaa", needle="bba"))

"""
Runtime: 28 ms, faster than 75.55% of Python3 online submissions for Implement strStr().
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Implement strStr().
"""