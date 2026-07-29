---
title: Search a 2D Matrix
source: NeetCode 150
pattern: Binary Search
date: 2026-07-29
language: Python
---

## 접근법

- 행의 첫 번째 원소를 기준으로 target이 포함될 가능성이 있는 행을 이진 탐색한다.
- 후보 행을 정한 뒤 해당 행에서 열 이진 탐색을 수행한다.
- 행 탐색과 열 탐색을 각각 독립적으로 수행해 탐색 범위를 줄인다.

## 시간·공간 복잡도

- 시간 복잡도: O(log m + log n)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- 2차원 정렬 행렬은 먼저 후보 행을 찾고, 그 행 안에서 다시 이진 탐색하면 된다.
