---
title: Two Sum
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-20
language: Python
---

# Two Sum

## 처음 접근

각 숫자 뒤쪽 리스트에서 `target - nums[i]`를 찾았다.

```python
if target - nums[i] in nums[i + 1:]:
```

찾은 값의 실제 인덱스는 잘린 리스트 기준이므로 `i + 1`을 더해 보정했다.

```python
i + 1 + nums[i + 1:].index(target - nums[i])
```

정답이지만, 매번 리스트를 자르고 탐색하므로 느리다.

## 발전한 접근

이미 본 숫자를 `dict`에 `숫자: 인덱스`로 저장한다.

```python
for i, num in enumerate(nums):
    need = target - num

    if need in seen:
        return [seen[need], i]

    seen[num] = i
```

`enumerate(nums)`는 인덱스 `i`와 값 `num`을 함께 꺼낸다.

## 시간·공간 복잡도

- 처음 접근: 시간 `O(n²)`
- dict 접근: 시간 `O(n)`, 공간 `O(n)`

## 다음에 기억할 한 줄

두 수의 합을 빠르게 찾을 때는 이전 숫자를 `dict`에 `숫자: 인덱스`로 저장한다.
