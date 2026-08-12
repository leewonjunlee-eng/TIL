---
title: Count Good Nodes in Binary Tree
source: NeetCode 150
pattern: Tree
date: 2026-08-12
language: Python
---

## 접근법

- DFS로 트리를 순회하면서 루트부터 현재 노드까지의 최댓값을 함께 전달한다.
- 현재 노드의 값이 경로의 최댓값보다 크거나 같으면 good node로 판단한다.
- good node를 만나면 `answer`를 1 증가시킨다.
- 자식 노드로 내려갈 때 현재 노드까지의 최댓값을 전달한다.
- 카운터 정수 `answer`를 변경하므로 중첩 함수에서 `nonlocal`을 사용한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(h), 재귀 호출 스택

## 다음에 기억할 한 줄

- 각 노드의 good 여부는 루트부터 현재 노드까지의 경로 최댓값과 비교하면 한 번의 DFS로 판단할 수 있다.
