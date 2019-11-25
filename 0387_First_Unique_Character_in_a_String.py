"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        non_repeat_char = []
        repeat_char = []

        for c in s:
            if c not in non_repeat_char:
                if c not in repeat_char:
                    non_repeat_char.append(c)
            else:
                non_repeat_char.remove(c)
                repeat_char.append(c)

        if len(non_repeat_char) > 0:
            return s.find(non_repeat_char[0])
        else:
            return -1


s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))

"""
Runtime: 208 ms, faster than 8.98% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
"""
