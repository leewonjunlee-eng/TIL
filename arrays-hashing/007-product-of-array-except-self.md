---
title: Product of Array Except Self
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-22
language: Python
---


# Product of Array Except Self


## 접근법


각 위치에서 자기 자신을 제외한 모든 원소의 곱을 구해야 한다.


처음에는 전체 곱을 구한 뒤 현재 값을 나누는 방법을 생각할 수 있다. 하지만 문제에서 나눗셈 사용을 금지했고, 0이 포함되면 별도 예외 처리가 필요하다. 그래서 왼쪽 누적 곱과 오른쪽 누적 곱을 나누어 계산했다.


answer는 반환 배열이면서 왼쪽 누적 곱을 저장하는 공간으로 사용한다.


### 1. 왼쪽 누적 곱 저장


먼저 모든 값을 1로 채운 answer를 만든다. postfix 변수는 현재 위치의 왼쪽에 있는 값들의 곱을 저장한다.


    answer = [1] * len(nums)
    postfix = 1


현재 숫자를 answer에 곱하지 않고, 다음 위치에 누적 곱을 저장한다.


    for index in range(len(answer) - 1):
        postfix *= nums[index]
        answer[index + 1] *= postfix


예를 들어 nums가 [1, 2, 3, 4]라면 첫 번째 순회가 끝난 뒤 answer에는 다음과 같이 저장된다.
