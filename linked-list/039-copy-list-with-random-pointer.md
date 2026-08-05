---
title: Copy List with Random Pointer
source: NeetCode 150
pattern: Linked List / Hash Map
date: 2026-08-05
language: Python
---

## 접근법

- 첫 순회에서 원본 리스트와 같은 값·`next` 구조의 복제 리스트를 만들고, `원본 노드: 복제 노드`를 딕셔너리에 저장한다.
- 두 번째 순회에서 `copies[original.random]`으로 복제 노드의 `random` 포인터를 연결한다.
- `copies = {None: None}`을 넣어 `random`이 없는 노드도 같은 코드로 처리한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(n)

## 막힌 지점 또는 틀린 이유

- 딕셔너리 저장은 원본·복제 포인터를 만든 뒤에 해야 한다. `copies[original] = current`은 현재 만든 복제 노드를 저장한다.

## 다음에 기억할 한 줄

- `random` 포인터는 원본 노드가 아니라 딕셔너리에서 찾은 복제 노드에 연결한다.
