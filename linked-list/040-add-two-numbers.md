---
title: Add Two Numbers
source: NeetCode 150
pattern: Linked List / Math
date: 2026-08-05
language: Python
---

## 접근법

- `dummy`, `tail`로 결과 연결 리스트를 앞에서부터 만든다.
- 각 자리의 합은 `left.val + right.val + carry`로 계산한다.
- `total % 10`은 현재 자리, `total // 10`은 다음 자리의 `carry`다.
- 한 리스트가 먼저 끝나거나 마지막 `carry`가 남는 경우까지 `while left or right or carry`로 처리한다.

## 시간·공간 복잡도

- 시간 복잡도: O(max(m, n))
- 공간 복잡도: O(max(m, n)) — 반환 리스트 제외 시 O(1)

## 막힌 지점 또는 틀린 이유

- `carry`는 `% 10` 전에 합쳐야 한다. 마지막 `carry`도 새 노드가 필요할 수 있다.

## 다음에 기억할 한 줄

- 연결 리스트 덧셈은 `total`, `digit`, `carry`를 매 자리 반복한다.
