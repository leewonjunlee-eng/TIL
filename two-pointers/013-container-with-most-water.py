from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calculate_area(left_height, right_height, left, right):
            height = min(left_height, right_height)
            width = right - left
            return height * width

        left = 0
        right = len(heights) - 1
        best = 0

        while left < right:
            total = calculate_area(
                heights[left],
                heights[right],
                left,
                right,
            )
            total_left = calculate_area(
                heights[left + 1],
                heights[right],
                left + 1,
                right,
            )
            total_right = calculate_area(
                heights[left],
                heights[right - 1],
                left,
                right - 1,
            )
            total_middle = calculate_area(
                heights[left + 1],
                heights[right - 1],
                left + 1,
                right - 1,
            )

            if total > best:
                best = total

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return best
