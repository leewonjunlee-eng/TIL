from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(values: List[str]) -> bool:
            values = [value for value in values if value != "."]
            return len(values) == len(set(values))

        # 행 검사
        for row in board:
            if not is_valid(row):
                return False

        # 열 검사
        for column in range(9):
            values = [board[row][column] for row in range(9)]
            if not is_valid(values):
                return False

        # 3 x 3 박스 검사
        for row_start in range(0, 9, 3):
            for column_start in range(0, 9, 3):
                values = []

                for row in range(row_start, row_start + 3):
                    for column in range(column_start, column_start + 3):
                        values.append(board[row][column])

                if not is_valid(values):
                    return False

        return True
