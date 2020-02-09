"""
https://leetcode.com/problems/keys-and-rooms/

There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1,
and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i],
and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.
A key rooms[i][j] = v opens the room with number v.


Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.

Example 2:

Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
Note:

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
The number of keys in all rooms combined is at most 3000.
"""


class Solution(object):
    def __init__(self):
        self.chk_rooms = []
        self.open_rooms = []
        self.rooms = []
        self.open_rooms_cnt = 0

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        self.chk_rooms = [0] * len(rooms)
        self.open_rooms = [0] * len(rooms)
        self.rooms = rooms

        self.open_room(0)

        if self.open_rooms_cnt == len(rooms):
            return True
        else:
            return False

    def open_room(self, chk_room):
        if self.chk_rooms[chk_room] == 0:
            self.chk_rooms[chk_room] = 1
            self.open_rooms_cnt += 1

            for i in self.rooms[chk_room]:
                self.open_room(i)


s = Solution()
print(s.canVisitAllRooms([[1], [2], [3], []]))
print(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))

"""
Runtime: 40 ms, faster than 98.24% of Python online submissions for Keys and Rooms.
Memory Usage: 12.4 MB, less than 66.67% of Python online submissions for Keys and Rooms.
"""
