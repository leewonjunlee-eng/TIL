---
title: Subtree of Another Tree
source: NeetCode 150
pattern: Tree
date: 2026-08-11
language: Python
---

## 접근법

- 현재 `root`를 기준으로 `subRoot`와 같은 트리인지 `isSameTree`로 확인한다.
- 현재 위치에서 같으면 `True`를 반환한다.
- 다르면 `root`의 왼쪽과 오른쪽 subtree에서 같은 과정을 반복한다.
- `isSameTree`를 재사용해 값뿐 아니라 구조까지 비교한다.

## 시간·공간 복잡도

- 시간 복잡도: O(n × m)
- 공간 복잡도: O(h_root + h_subRoot), 재귀 호출 스택

## 다음에 기억할 한 줄

- 특정 값이 있는지만 찾는 것이 아니라 해당 위치에서 `subRoot` 전체의 값과 구조가 같은지 확인해야 한다.
