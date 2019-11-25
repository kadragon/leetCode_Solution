"""
https://leetcode.com/problems/sort-characters-by-frequency/

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import operator


class Solution:
    def frequencySort(self, s: str) -> str:
        counting_data = self.count_char(s)
        sorted_counting = sorted(counting_data.items(), key=operator.itemgetter(1), reverse=True)

        ans = ""
        for key, value in sorted_counting:
            ans = ans + (key * value)

        return ans

    def count_char(self, s: str) -> dict:
        char_counting = {}

        for c in s:
            try:
                char_counting[c] += 1
            except KeyError:
                char_counting[c] = 1

        return char_counting


s = Solution()
print(s.frequencySort("tree"))
print(s.frequencySort("cccaaa"))
print(s.frequencySort("Aabb"))

"""
Runtime: 40 ms, faster than 91.54% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 13.6 MB, less than 92.86% of Python3 online submissions for Sort Characters By Frequency.
"""
