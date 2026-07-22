---
title: Valid Sudoku
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-22
language: Python
---

# Valid Sudoku

## 접근법

행, 열, 3×3 박스를 각각 검사하고 빈칸 "."은 제외했다.

중복 검사 로직은 is_valid() 함수로 분리해 같은 검사를 재사용했다. 각 행과 열은 리스트로 만들고, 각 3×3 박스는 시작 위치를 3씩 증가시키며 순회했다.

## 시간·공간 복잡도

- 시간: O(n²) (9×9 고정 보드에서는 O(1))
- 공간: O(n²) — 검사할 값들을 임시 리스트와 set에 저장

## 다음에 기억할 한 줄

행·열·박스를 같은 중복 검사 함수로 분리하면 Sudoku 검증 로직을 깔끔하게 구성할 수 있다.
