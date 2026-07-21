---
title: Top K Frequent Elements
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-21
language: Python
---

# Top K Frequent Elements

## 접근법

먼저 check 딕셔너리에 각 숫자의 등장 횟수를 저장한다.

```python
check[num] = check.get(num, 0) + 1
```

check.get(num, 0)은 num이 이미 있으면 현재 횟수를 가져오고, 아직 없으면 0을 사용한다.

그 다음 bucket[등장 횟수]에 해당 숫자를 넣는다.

```python
bucket = [[] for _ in range(len(nums) + 1)]

for num, count in check.items():
    bucket[count].append(num)
```

예를 들어 1이 3번, 2가 2번, 3이 1번 나왔다면 bucket[1] = [3], bucket[2] = [2], bucket[3] = [1]처럼 저장된다.

가장 많이 나온 숫자부터 필요하므로 큰 인덱스부터 거꾸로 순회한다.

```python
for count in range(len(bucket) - 1, 0, -1):
```

range(시작, 끝_직전, 변화량)에서 변화량이 -1이므로 마지막 인덱스부터 1까지 감소하며 반복한다. bucket[0]에는 0번 등장한 숫자가 없어서 확인하지 않는다.

## 시간·공간 복잡도

- 시간: O(n)
- 공간: O(n)

## 정렬 방식과 비교

빈도 딕셔너리를 sorted()로 정렬해도 풀 수 있지만 O(n log n)이 걸린다. bucket sort는 빈도의 최댓값이 len(nums)를 넘지 않는다는 점을 이용해 O(n)에 해결한다.

## 다음에 기억할 한 줄

빈도를 인덱스로 쓰는 bucket을 만들면, 정렬하지 않고도 가장 자주 나온 값부터 꺼낼 수 있다.
