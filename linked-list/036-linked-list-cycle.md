---
title: Linked List Cycle
source: NeetCode 150
pattern: Linked List
date: 2026-08-03
language: Python
---

## 접근법

- `slow`와 `fast`를 모두 `head`에서 시작한다.
- `slow`는 한 칸, `fast`는 두 칸씩 이동한다.
- cycle이 없으면 `fast` 또는 `fast.next`가 `None`이 되어 반복문이 끝난다.
- cycle이 있으면 빠른 포인터가 느린 포인터를 따라잡아 같은 노드에서 만난다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(1)

## 막힌 지점 또는 틀린 이유

- 처음에는 `fast = slow.next`로 작성했다. `slow`를 먼저 움직인 뒤라 두 포인터가 같은 노드를 가리킬 수 있어, `fast`는 자신의 위치에서 두 칸 이동해야 했다.

## 다음에 기억할 한 줄

- cycle 탐지는 `slow = slow.next`, `fast = fast.next.next`이고, 조건은 `while fast and fast.next`다.
