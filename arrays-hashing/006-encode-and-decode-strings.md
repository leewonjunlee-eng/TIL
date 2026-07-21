---
title: Encode and Decode Strings
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-21
language: Python
---

# Encode and Decode Strings

## 접근법

각 문자열 앞에 문자열의 길이와 `#`를 붙여 하나의 문자열로 만든다.

```python
str(len(word)) + "#" + word
```

예를 들어 `"neet"`은 `"4#neet"`가 된다. 문자열 안에 `#`가 들어 있어도 길이를 기준으로 읽으므로 안전하다.

디코딩할 때는 현재 위치에서 `#`를 찾고, 그 앞부분을 길이로 바꾼다.

```python
length = int(s[index:hash_index])
start = hash_index + 1
end = start + length
```

`s[start:end]`로 정확히 한 문자열을 꺼낸 뒤, 다음 문자열의 시작 위치인 `end`부터 다시 읽는다.

```python
index = end
```

## 시간·공간 복잡도

- 시간: `O(n)`
- 공간: `O(n)`

## 다음에 기억할 한 줄

구분자가 문자열 내용에 들어갈 수 있다면, 구분자만 쓰지 말고 문자열 길이도 함께 저장한다.
