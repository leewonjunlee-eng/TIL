---
title: Valid Anagram
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-20
language: Python
---

# Valid Anagram

## 접근법

문자열 `s`, `t` 각각에서 글자가 나온 횟수를 `dict`에 기록했다.

```python
counts = {"a": 2, "b": 1}
```

두 dict가 같으면 각 글자의 종류와 등장 횟수가 모두 같다는 뜻이므로 anagram이다.

```python
return counts == counts_2
```

## 시간·공간 복잡도

- 시간: `O(len(s) + len(t))`
- 공간: `O(len(s) + len(t))`

## 막힌 지점

처음에는 문자열에서 글자를 하나씩 지우는 방법을 생각했다. 가능하지만 매번 글자를 찾고 삭제하면 느려진다.

`dict`는 2차원 배열이 아니라 `키: 값` 형태다. 여기서는 `글자: 등장 횟수`를 저장했다.

두 dict를 쓰면 빠르지만 글자별 정보를 저장하므로 메모리를 더 쓴다. 시간과 메모리 사이의 트레이드오프다.

## 다음에 기억할 한 줄

문자별 등장 횟수를 비교할 때는 `dict`에 `글자: 횟수`를 저장한다.
