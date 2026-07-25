---
title: Longest Repeating Character Replacement
source: NeetCode 150
pattern: Sliding Window
date: 2026-07-25
language: Python
---

# Longest Repeating Character Replacement

## 접근법

오른쪽 포인터를 한 칸씩 이동하며 현재 window 안의 각 문자 개수를 센다.

window에서 가장 많이 나온 문자 하나를 남긴다고 생각하면, 나머지 문자를 바꾸는 데 필요한 횟수는 다음과 같다.

`window 길이 - 가장 많이 나온 문자 개수`

이 값이 `k`보다 크면 왼쪽 포인터를 이동해 window를 줄인다. 조건을 만족하는 window의 최대 길이를 갱신한다.

## 시간·공간 복잡도

- 시간: O(n)
- 공간: O(n)

오른쪽 포인터와 왼쪽 포인터가 각각 문자열을 한 번씩만 지나가므로 시간복잡도는 O(n)이다. 문자 개수를 저장하는 딕셔너리를 사용하므로 추가 공간복잡도는 O(n)이다.

## 막힌 지점 또는 틀린 이유

처음에는 가장 많이 나온 문자를 기준으로 window를 새로 시작하려고 했다. 하지만 중복이 생길 때마다 window를 초기화하면 기존의 유효한 구간을 잃을 수 있다.

window가 조건을 벗어날 때 왼쪽 포인터를 이동하며 필요한 만큼만 줄이는 방식이 더 적절하다.

## 다음에 기억할 한 줄

window 길이에서 가장 많이 나온 문자 개수를 뺀 값이 바꿔야 하는 문자의 수다.
