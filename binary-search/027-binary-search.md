---
title: Binary Search
source: NeetCode 150
pattern: Binary Search
date: 2026-07-29
language: Python
---

## 접근법

- 정렬된 배열에서 왼쪽과 오른쪽 경계를 설정한다.
- 두 경계의 가운데 인덱스 mid를 계산해 target과 비교한다.
- nums[mid]가 target보다 작으면 왼쪽 경계를 오른쪽으로 옮기고, 크면 오른쪽 경계를 왼쪽으로 옮긴다.
- left <= right인 동안 반복해 마지막 후보까지 확인한다.

## 시간·공간 복잡도

- 시간 복잡도: O(log n)
- 공간 복잡도: O(1)

## 막힌 지점 또는 틀린 이유

- while left < right로 작성하면 left == right인 마지막 후보를 검사하지 못할 수 있다.
- 닫힌 구간 [left, right]을 사용하는 경우 반복 조건은 left <= right여야 한다.

## 다음에 기억할 한 줄

- 정렬된 배열의 탐색 범위를 매번 절반으로 줄이면 이진 탐색은 O(log n)에 동작한다.
