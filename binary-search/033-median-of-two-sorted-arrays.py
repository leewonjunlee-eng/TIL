class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            left1 = nums1[i - 1] if i else float("-inf")
            right1 = nums1[i] if i < m else float("inf")
            left2 = nums2[j - 1] if j else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2:
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2

            if left1 > right2:
                right = i - 1
            else:
                left = i + 1

        raise ValueError("At least one array must be non-empty")


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([], [1]) == 1
