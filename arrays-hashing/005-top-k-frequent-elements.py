from typing import Dict, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check: Dict[int, int] = {}

        for num in nums:
            check[num] = check.get(num, 0) + 1

        bucket: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for num, count in check.items():
            bucket[count].append(num)

        answer: List[int] = []

        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                answer.append(num)

                if len(answer) == k:
                    return answer

        return answer


if __name__ == "__main__":
    solution = Solution()
    assert solution.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert solution.topKFrequent([1], 1) == [1]
    assert solution.topKFrequent([4, 4, 4, 4, 2, 2, 3, 3, 1], 3) == [4, 2, 3]
