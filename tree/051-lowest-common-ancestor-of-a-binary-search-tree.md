---
title: Lowest Common Ancestor of a Binary Search Tree
source: NeetCode 150
pattern: Tree
date: 2026-08-11
language: Python
---

## 접근법

- 두 노드의 값을 비교해 `p`가 더 큰 경우 두 노드를 swap한다.
- 현재 `root`의 값이 `p`와 `q`의 값 사이에 있으면 현재 노드가 LCA이므로 반환한다.
- `p`와 `q`가 모두 현재 노드보다 작으면 왼쪽 subtree로 이동한다.
- `p`와 `q`가 모두 현재 노드보다 크면 오른쪽 subtree로 이동한다.
- BST의 값 관계를 이용하므로 별도의 경로 저장 없이 탐색한다.

## 시간·공간 복잡도

- 시간 복잡도: O(h)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- BST에서는 두 노드가 현재 노드를 기준으로 같은 방향에 있는지 확인하면 LCA를 찾을 수 있다.
