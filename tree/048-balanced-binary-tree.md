---
title: Balanced Binary Tree
source: NeetCode 150
pattern: Tree
date: 2026-08-08
language: Python
---

## 접근법

- 각 subtree의 높이를 재귀적으로 계산한다.
- 왼쪽 또는 오른쪽 subtree가 이미 불균형이면 `-1`을 반환한다.
- 현재 노드에서 양쪽 높이 차이가 1보다 크면 `-1`을 반환한다.
- 균형 상태라면 부모에게 현재 subtree의 높이를 반환한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(h), 재귀 호출 스택

## 다음에 기억할 한 줄

- 높이 계산과 균형 검사를 한 번의 DFS에서 처리하고, `-1`로 불균형을 부모에게 전달한다.
