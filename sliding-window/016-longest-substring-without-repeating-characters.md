---
title: Longest Substring Without Repeating Characters
source: NeetCode 150
pattern: Sliding Window
date: 2026-07-25
language: Python
---

# Longest Substring Without Repeating Characters

## 접근법

문자열을 왼쪽에서 오른쪽으로 순회하면서 중복이 없는 현재 window를 유지한다.

새 문자가 이미 window 안에 있으면 왼쪽 포인터를 이동하면서 해당 문자를 제거한다. 중복이 사라지면 새 문자를 추가하고 현재 window의 길이로 최댓값을 갱신한다.

## 시간·공간 복잡도

- 시간: O(n)
- 공간: O(n)

문자열의 각 문자가 set에 추가되고 최대 한 번 제거되므로 시간복잡도는 O(n)이다. 중복 여부를 빠르게 확인하기 위해 set을 사용하므로 추가 공간복잡도는 O(n)이다.

## 막힌 지점 또는 틀린 이유

처음에는 리스트를 사용해 중복 여부를 확인하고, 중복 문자를 만나면 리스트를 잘라냈다. 리스트의 `in`, `index`, 슬라이싱은 각각 선형 시간이 걸릴 수 있다.

set의 `in`은 평균 O(1)이므로 set과 왼쪽 포인터를 사용해 시간복잡도를 O(n)으로 줄였다.

## 다음에 기억할 한 줄

중복이 생기면 window 전체를 다시 만들지 말고 왼쪽 포인터를 이동하며 중복이 사라질 때까지 줄인다.
