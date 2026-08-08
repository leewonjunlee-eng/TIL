---
title: Maximum Depth of Binary Tree
source: NeetCode 150
pattern: Tree
date: 2026-08-08
language: Python
---

## 접근법

- 현재 노드가 없으면 깊이 `0`을 반환한다.
- 왼쪽 subtree와 오른쪽 subtree의 최대 깊이를 각각 구한다.
- 현재 노드를 포함하기 위해 더 큰 깊이에 `1`을 더한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(h), 재귀 호출 스택

## 다음에 기억할 한 줄

- 현재 노드의 깊이는 왼쪽·오른쪽 subtree 중 더 깊은 쪽에 1을 더한 값이다.
