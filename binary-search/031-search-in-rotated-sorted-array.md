---
title: Search in Rotated Sorted Array
source: NeetCode 150
pattern: Binary Search
date: 2026-07-30
language: Python
---

## 접근법

- 매 반복마다 왼쪽 절반 또는 오른쪽 절반 중 정렬된 구간을 찾는다.
- 정렬된 구간 안에 target이 있으면 그 구간을 탐색하고, 없으면 반대쪽을 탐색한다.
- `nums[left] <= nums[mid]`이면 왼쪽 구간이 정렬되어 있다는 뜻이다.

## 시간·공간 복잡도

- 시간 복잡도: O(log n)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- 회전된 배열도 매번 정렬된 절반을 찾으면 이진 탐색을 적용할 수 있다.
