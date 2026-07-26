from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        answer = []

        for right in range(len(nums)):
            left = right - k + 1

            # 윈도우를 벗어난 인덱스 제거
            while dq and dq[0] < left:
                dq.popleft()

            # 현재 값보다 작거나 같은 값은 최댓값 후보에서 제거
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # 윈도우 크기가 k가 된 순간부터 최댓값 추가
            if right >= k - 1:
                answer.append(nums[dq[0]])

        return answer
