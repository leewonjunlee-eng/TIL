---
title: Product of Array Except Self
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-22
language: Python
---

# Product of Array Except Self

## 접근법

나눗셈 없이 왼쪽 누적 곱과 오른쪽 누적 곱을 두 번 순회하며 계산했다.

첫 번째 순회에서는 현재 원소의 왼쪽에 있는 값들의 곱을 `answer`에 저장한다. 두 번째 순회에서는 오른쪽 누적 곱을 곱해 현재 원소를 제외한 전체 곱을 완성한다.

## 시간·공간 복잡도

- 시간: `O(n)`
- 공간: `O(1)` — 반환 배열을 제외한 추가 공간

## 다음에 기억할 한 줄

나눗셈 없이도 prefix와 postfix 누적 곱을 결합하면 각 원소를 제외한 곱을 구할 수 있다.
