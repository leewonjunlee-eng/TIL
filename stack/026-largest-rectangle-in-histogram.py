class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        best = 0
        for index,height in enumerate(heights):
            while stack and stack[-1][0] > height:

                now_height, _ = stack.pop()
                if stack:
                    now_index = stack[-1][1]
                else:
                    now_index = -1
                if best < now_height * (index - now_index-1):
                    best = now_height * (index - now_index-1)

            stack.append((height,index))

        return best
