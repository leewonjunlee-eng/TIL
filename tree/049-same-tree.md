---
title: Same Tree
source: NeetCode 150
pattern: Tree
date: 2026-08-11
language: Python
---

## 접근법

- 두 노드가 모두 비어 있으면 같은 subtree이므로 `True`를 반환한다.
- 한쪽 노드만 비어 있으면 구조가 다르므로 `False`를 반환한다.
- 두 노드의 값이 다르면 `False`를 반환한다.
- 현재 노드가 같으면 왼쪽과 오른쪽 subtree를 동시에 재귀적으로 비교한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(h), 재귀 호출 스택

## 다음에 기억할 한 줄

- 순회 결과만 비교하지 말고 빈 노드 여부와 현재 값 및 양쪽 subtree를 함께 비교해야 트리의 구조까지 확인할 수 있다.
