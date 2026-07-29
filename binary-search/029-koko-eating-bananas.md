---
title: Koko Eating Bananas
source: NeetCode 150
pattern: Binary Search
date: 2026-07-29
language: Python
---

## 접근법

- 시간당 먹는 바나나 수를 기준으로 이진 탐색한다.
- 각 속도에서 모든 더미를 먹는 데 필요한 총 시간을 계산한다.
- 총 시간이 h 이하라면 더 느린 속도도 가능한지 확인하고, h를 초과하면 속도를 높인다.

## 시간·공간 복잡도

- 시간 복잡도: O(n log m)
- 공간 복잡도: O(1)

## 다음에 기억할 한 줄

- 정답이 숫자 범위 안에 있고 가능 여부를 판단할 수 있으면 정답 자체를 이진 탐색할 수 있다.
