---
title: Remove Nth Node From End of List
source: NeetCode 150
pattern: Linked List / Two Pointers
date: 2026-08-05
language: Python
---

## 접근법

- `dummy`를 `head` 앞에 붙여서 첫 노드 삭제도 같은 방식으로 처리한다.
- `fast`를 먼저 `n`칸 이동한 뒤, `fast`가 끝에 도달할 때까지 `slow`, `fast`를 함께 이동한다.
- 그때 `slow`는 삭제할 노드 바로 앞에 있으므로 `slow.next = slow.next.next`로 건너뛴다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- 끝에서 n번째를 삭제할 때는 `dummy`를 두고, `fast`를 n칸 먼저 보내면 된다.
