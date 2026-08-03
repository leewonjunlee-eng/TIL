---
title: Merge Two Sorted Linked Lists
source: NeetCode 150
pattern: Linked List
date: 2026-08-03
language: Python
---

## 접근법

- 새 Python 리스트에 값을 넣지 않고, 두 입력 연결 리스트의 기존 노드를 결과에 다시 연결한다.
- 첫 노드를 따로 처리하지 않기 위해 임시 시작 노드 `dummy`를 만들고, `now`가 결과의 현재 끝을 가리키게 한다.
- `cur1`, `cur2`가 모두 있을 때 값이 더 작은 노드를 `now.next`에 연결하고, 연결한 리스트만 다음 노드로 이동한다.
- 비교가 끝나면 남은 한쪽은 이미 정렬되어 있으므로 `now.next = cur1 or cur2`로 통째로 연결한다.
- `dummy`는 임시 노드이므로 실제 결과의 시작점인 `dummy.next`를 반환한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n + m)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- 두 정렬 리스트는 작은 현재 노드를 뒤에 연결하고, 남은 한쪽은 `cur1 or cur2`로 한 번에 붙인다.
