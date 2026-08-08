---
title: Invert Binary Tree
source: NeetCode 150
pattern: Tree
date: 2026-08-08
language: Python
---

## 접근법

- 현재 노드가 없으면 `None`을 반환한다.
- 현재 노드의 왼쪽 자식과 오른쪽 자식을 교환한다.
- 교환한 왼쪽 subtree와 오른쪽 subtree를 재귀적으로 뒤집는다.
- 전위 순회 방식으로 현재 노드를 먼저 처리한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(h), 재귀 호출 스택

## 막힌 지점 또는 틀린 이유

- `return None`은 빈 subtree에 도달했을 때 해당 재귀 호출을 종료하는 종료 조건이다.
- 자식 노드를 먼저 재귀 호출하기보다 현재 노드에서 `left`와 `right`를 먼저 교환한 뒤 내려간다.
- 트리 자체를 수정한 뒤 마지막에 원래 root를 반환한다.

## 다음에 기억할 한 줄

- 현재 노드의 자식을 swap하고, 왼쪽·오른쪽 subtree에 같은 작업을 반복한다.
