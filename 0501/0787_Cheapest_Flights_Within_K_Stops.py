"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""


class Solution:
    def __init__(self):
        self.flights_list = []
        self.able_flights = []
        self.dst = None
        self.K = None
        self.min_value = -1

    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, K: int) -> int:
        self.dst = dst
        self.K = K

        for _ in range(n):
            self.flights_list.append([-1] * n)
            self.able_flights.append([])

        for u, v, w in flights:
            try:
                self.flights_list[u][v] = w
                self.able_flights[u].append(v)

            except KeyError:
                return -1

        if K == 0:
            try:
                return self.flights_list[src][dst]
            except KeyError:
                return -1

        check_list = [0] * n
        self.find_way(src, check_list, 0, 0, 0)

        return self.min_value

    def find_way(self, now: int, check_list: [], k: int, value: int, post):
        check_list[now] = 1

        if k > self.K:
            return None

        for a in self.able_flights[now]:
            tmp_check_list = check_list.copy()
            if tmp_check_list[a] != 1:
                tmp_check_list[a] = 1
                tmp_value = value + self.flights_list[now][a]

                if self.min_value != -1 and tmp_value >= self.min_value:
                    continue

                if a == self.dst:
                    if self.min_value == -1 or self.min_value > tmp_value:
                        self.min_value = tmp_value
                    else:
                        return None

                self.find_way(a, tmp_check_list, k + 1, tmp_value, now)


s = Solution()
print(s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
s = Solution()
print(s.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))

"""
Runtime: 1892 ms, faster than 5.02% of Python3 online submissions for Cheapest Flights Within K Stops.
Memory Usage: 13.6 MB, less than 94.74% of Python3 online submissions for Cheapest Flights Within K Stops.
"""