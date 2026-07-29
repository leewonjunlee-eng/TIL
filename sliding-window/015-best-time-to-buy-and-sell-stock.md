---
title: Best Time to Buy and Sell Stock
source: NeetCode 150
pattern: Sliding Window
date: 2026-07-25
language: Python
---

# Best Time to Buy and Sell Stock

## 접근법

왼쪽에서 오른쪽으로 한 번 순회하면서 지금까지의 최저 매수가를 저장한다.

현재 가격에서 최저 매수가를 뺀 값을 현재 이익으로 계산하고, 지금까지의 최대 이익과 비교해 갱신한다. 최저 매수가보다 더 낮은 가격을 만나면 최저 매수가를 바꾼다.

## 시간·공간 복잡도

- 시간: O(n)
- 공간: O(1)

가격 리스트를 한 번만 순회하므로 시간복잡도는 O(n)이다. 최저 가격과 최대 이익만 저장하므로 추가 공간복잡도는 O(1)이다.

## 다음에 기억할 한 줄

각 날짜에서는 지금까지 가장 싼 가격에 샀다고 가정하고 현재 가격에 팔았을 때의 이익을 계산한다.
