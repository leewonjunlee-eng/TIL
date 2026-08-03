---
title: Reverse Linked List
source: NeetCode 150
pattern: Linked List
date: 2026-08-03
language: Python
---

## 접근법

- 연결 리스트는 새 리스트에 값을 `append()`하는 대신, 기존 노드의 `next` 연결을 반대로 바꾼다.
- `prev`는 이미 뒤집은 부분의 시작 노드, `current`는 현재 처리할 노드다.
- `current.next`를 바꾸기 전에 `cur_next`에 저장한다. 바로 연결을 바꾸면 원래 다음 노드로 갈 길을 잃기 때문이다.
- 모든 노드를 처리한 뒤 `prev`가 새 head이므로 반환한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- 연결을 뒤집기 전 다음 노드를 `cur_next`에 임시 저장하고, 마지막에는 새 head인 `prev`를 반환한다.
