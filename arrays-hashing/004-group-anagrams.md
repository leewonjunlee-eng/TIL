---
title: Group Anagrams
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-21
language: Python
---

# Group Anagrams

## 접근법

애너그램은 글자의 종류와 개수가 같고 순서만 다르다. 따라서 각 단어의 글자를 정렬한 문자열을 그룹을 찾는 key로 사용했다.

```python
key = ''.join(sorted(word))
```

`"eat"`, `"tea"`, `"ate"`는 모두 정렬하면 `"aet"`가 된다.

`check`에는 `정렬된 key: answer 안의 그룹 인덱스`를 저장한다. 이미 같은 key가 있으면 해당 안쪽 리스트에 단어를 추가하고, 없으면 새 그룹을 만든다.

```python
if key in check:
    answer[check[key]].append(word)
else:
    check[key] = len(answer)
    answer.append([word])
```

## 시간·공간 복잡도

- 시간: `O(n × k log k)`
  - 단어가 `n`개이고, 한 단어의 평균 길이가 `k`일 때 각 단어를 정렬한다.
- 공간: `O(n × k)`
  - 결과 그룹과 정렬 key를 저장한다.

## 더 빠른 방법

문제가 영어 소문자만 다룬다면 26칸짜리 글자 수 배열을 만들고 `tuple`로 바꿔 key로 쓸 수 있다. 이 방법은 정렬을 하지 않아 시간 복잡도를 `O(n × k)`로 줄일 수 있다.

다만 정렬 key 방식은 더 직관적이고, 문자 종류가 제한되지 않아도 그대로 사용할 수 있다.

## 다음에 기억할 한 줄

애너그램을 여러 그룹으로 묶을 때는 각 단어를 정렬한 값을 dict의 key로 사용한다.
