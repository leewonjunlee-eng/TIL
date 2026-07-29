---
title: Longest Consecutive Sequence
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-22
language: Python
---

# Longest Consecutive Sequence

## 문제

정렬되지 않은 정수 배열 `nums`가 주어질 때, 가장 긴 연속된 숫자들의 길이를 반환한다.

연속된 숫자란 `1, 2, 3, 4`처럼 숫자가 1씩 증가하는 수열이다.
알고리즘의 시간복잡도는 O(n)이어야 한다.

## 접근법

먼저 `set(nums)`를 만들어 중복을 제거하고 숫자 존재 여부를 빠르게 확인한다.

각 숫자 `num`에 대해 `num - 1`이 set에 없을 때만 수열의 시작점으로 판단한다.
시작점이라면 `num + 1`, `num + 2`가 set에 존재하는 동안 길이를 증가시킨다.

`for` 안에 `while`이 있지만, 수열의 시작점에서만 `while`을 실행하므로 전체 확인 횟수는 평균적으로 O(n)이다.

## 시간·공간 복잡도

- 시간: 평균 O(n)
- 공간: O(n)

## 코드

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        answer = 0

        for num in numbers:
            if num - 1 not in numbers:
                length = 1
                while num + length in numbers:
                    length += 1
                answer = max(answer, length)

        return answer
```

## 한 줄 정리

set의 평균 O(1) 검색을 이용해 수열의 시작점만 탐색하면 정렬 없이 O(n)에 해결할 수 있다.
