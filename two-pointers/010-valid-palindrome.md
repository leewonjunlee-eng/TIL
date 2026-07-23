---
title: Valid Palindrome
source: NeetCode 150
pattern: Two Pointers
date: 2026-07-23
language: Python
---

# Valid Palindrome

## 접근법

문자열에서 알파벳과 숫자만 남기고 모두 소문자로 변환했다. 그 결과를 앞에서 읽은 리스트와 뒤에서 읽은 리스트로 각각 만든 뒤 두 리스트가 같은지 비교했다.

```python
filtered = "".join(char.lower() for char in s if char.isalnum())
```

## 시간·공간 복잡도

- 시간: `O(n)`
- 공간: `O(n)`

문자열 전체를 확인해야 하므로 시간복잡도 `O(n)`은 최적이다. `filtered`, `forward`, `backward`를 만들기 때문에 추가 공간은 `O(n)`이다.

## 막힌 지점 또는 틀린 이유

문자열을 뒤에서부터 순회할 때 `reversed(filtered)`를 사용한다.

## 다음에 기억할 한 줄

시간 `O(n)`은 유지하면서 공간을 줄이고 싶다면, 문자열을 새로 만들지 않고 양쪽 포인터로 직접 비교한다.
