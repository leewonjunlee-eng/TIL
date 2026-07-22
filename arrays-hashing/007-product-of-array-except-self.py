from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        postfix = 1

        for index in range(len(answer) - 1):
            postfix *= nums[index]
            answer[index + 1] *= postfix

        postfix = 1

        for index in range(len(answer) - 1, 0, -1):
            postfix *= nums[index]
            answer[index - 1] *= postfix

        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
