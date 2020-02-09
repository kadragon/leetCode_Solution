"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled,
where empty cells are filled with the character '.'.
"""


def check_repetition(value):
    digits_list = list("123456789")
    for i in value:
        if i != '.':
            try:
                digits_list.remove(i)
            except ValueError:
                return False

    return True


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if check_repetition(row) is False:
                return False

        for i in range(0, 9):
            tmp_list = []
            for j in range(0, 9):
                tmp_list.append(board[j][i])

            if check_repetition(tmp_list) is False:
                return False

        check_point = [0, 3, 6]

        for i in check_point:
            for j in check_point:
                tmp_list = []
                for k in [0, 1, 2]:
                    for l in [0, 1, 2]:
                        tmp_list.append(board[i + k][j + l])

                if check_repetition(tmp_list) is False:
                    return False

        return True


s = Solution()

test_value = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(s.isValidSudoku(test_value))

test_value_2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

print(s.isValidSudoku(test_value_2))

"""
Runtime: 92 ms, faster than 22.39% of Python online submissions for Valid Sudoku.
Memory Usage: 11.7 MB, less than 88.00% of Python online submissions for Valid Sudoku.
"""
