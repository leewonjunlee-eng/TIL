---
title: Time Based Key-Value Store
source: NeetCode 150
pattern: Binary Search
date: 2026-07-30
language: Python
---

## 접근법

- `key`별로 `(timestamp, value)` 기록을 리스트에 저장한다.
- 같은 `key`의 timestamp는 증가하는 순서로 주어지므로 별도 정렬이 필요 없다.
- `get()`에서는 timestamp가 현재 시점 이하인 기록 중 가장 최근 값을 이진 탐색으로 찾는다.
- 탐색 중 조건을 만족하면 결과 후보로 저장하고, 더 최신 기록이 있는지 오른쪽을 계속 탐색한다.

## 시간·공간 복잡도

- `set()` 시간 복잡도: O(1)
- `get()` 시간 복잡도: O(log n)
- 공간 복잡도: O(n)

## 다음에 기억할 한 줄

- 조건을 만족하는 값 중 가장 오른쪽 값을 찾을 때는 후보를 저장하고 오른쪽으로 더 탐색한다.
