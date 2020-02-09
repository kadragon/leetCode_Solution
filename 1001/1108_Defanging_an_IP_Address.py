"""
https://leetcode.com/problems/defanging-an-ip-address/

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".


Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:
The given address is a valid IPv4 address.
"""


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address_list = address.replace('"', '').split('.')
        return '[.]'.join(address_list)


s = Solution()
result = s.defangIPaddr(address="1.1.1.1")
print(result)

"""
Runtime: 12 ms, faster than 87.19% of Python online submissions for Defanging an IP Address.
Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Defanging an IP Address.
"""
