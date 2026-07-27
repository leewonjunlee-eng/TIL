---
title: Min Stack
source: NeetCode 150
pattern: Stack
date: 2026-07-27
language: Python
---

## 접근법

- 실제 값은 stack에, 현재까지의 최솟값은 min_stack에 함께 저장한다.
- push할 때 현재 최솟값을 기록하고, pop할 때 두 스택에서 함께 제거한다.
- min_stack의 마지막 값이 현재 스택의 최솟값이다.

## 시간·공간 복잡도

- 시간 복잡도: 각 연산 O(1)
- 공간 복잡도: O(n)

## 막힌 지점 또는 틀린 이유

- 최솟값 하나만 저장하면 그 값이 pop된 뒤 이전 최솟값을 알 수 없다.
- 각 push 시점의 최솟값을 min_stack에 기록해야 이전 상태를 복원할 수 있다.

## 다음에 기억할 한 줄

최솟값도 스택처럼 과거 상태를 순서대로 저장한다.
