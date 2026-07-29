---
title: Find Minimum in Rotated Sorted Array
source: NeetCode 150
pattern: Binary Search
date: 2026-07-29
language: Python
---

## 접근법

- 중간값과 오른쪽 끝값을 비교해 최솟값이 있는 구간을 좁힌다.
- 중간값이 오른쪽 끝값보다 크면 최솟값은 중간값의 오른쪽에 있다.
- 그렇지 않으면 중간값을 포함한 왼쪽 구간에 최솟값이 있다.

## 시간·공간 복잡도

- 시간 복잡도: O(log n)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- 회전된 정렬 배열에서는 한쪽 끝값과 중간값을 비교하면 회전 지점을 포함하는 구간을 알 수 있다.
