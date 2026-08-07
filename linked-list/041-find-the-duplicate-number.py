from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    solution = Solution()
    assert solution.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert solution.findDuplicate([1, 1]) == 1
    assert solution.findDuplicate([2, 2, 2, 2, 2]) == 2
    assert solution.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]) == 9
