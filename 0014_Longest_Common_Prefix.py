"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        try:
            min_len = len(min(strs))
        except ValueError:
            return ""

        prefix = 0
        end_flag = False
        for k in range(min_len):
            for in_str in strs:
                if in_str[0:prefix+1] != strs[0][0:prefix+1]:

                    end_flag = True
                    break

            if end_flag:
                break
            else:
                prefix += 1

        return strs[0][0:prefix]


s = Solution()
result = s.longestCommonPrefix(["dog", "racecar", "car"])
print(result)

result = s.longestCommonPrefix(["flower", "flow", "flight"])
print(result)

result = s.longestCommonPrefix(["a"])
print(result)
