from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.hasDuplicate([1, 2, 3, 1]) is True
    assert solution.hasDuplicate([1, 2, 3, 4]) is False
