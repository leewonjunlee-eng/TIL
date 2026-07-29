class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid
            else:
                right = mid - 1

        if matrix[right][0] == target:
            return True

        if target > matrix[right][0] and left != right:
            first = right
        else:
            first = left

        left = 0
        right = len(matrix[first]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[first][mid] == target:
                return True
            elif matrix[first][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
