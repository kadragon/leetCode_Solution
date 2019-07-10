"""
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        # 인덱스를 활용하는 리스트 생성
        low_data = [1] * n

        # 리스트를 돌아다니면서 x의 배수는 0으로 표기
        for x in range(2, n):
            if low_data[x] == 1:
                for y in range(2, n//x+1):
                    try:
                        low_data[x*y] = 0
                    except IndexError:
                        continue

        return low_data[2:].count(1)


s = Solution()
print(s.countPrimes(0))
print(s.countPrimes(2))
print(s.countPrimes(11))
print(s.countPrimes(10000))