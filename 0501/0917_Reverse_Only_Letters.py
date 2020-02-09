"""
https://leetcode.com/problems/reverse-only-letters/

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
and all letters reverse their positions.


Example 1:
Input: "ab-cd"
Output: "dc-ba"

Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letter_only_list = []
        no_letter_save = [None] * len(S)
        for i in range(len(S)):
            if S[i].isalpha():
                letter_only_list.append(S[i])
            else:
                no_letter_save[i] = S[i]

        for i in range(len(S)):
            if no_letter_save[i] is None:
                no_letter_save[i] = letter_only_list.pop()

        return ''.join(no_letter_save)


s = Solution()
print(s.reverseOnlyLetters("ab-cd"))
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))

"""
Runtime: 28 ms, faster than 67.56% of Python3 online submissions for Reverse Only Letters.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Reverse Only Letters.
"""

"""
Solution Hint
letters = [c for c in S if c.isalpha()]
"""