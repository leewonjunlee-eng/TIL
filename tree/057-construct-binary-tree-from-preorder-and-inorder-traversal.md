---
title: Construct Binary Tree from Preorder and Inorder Traversal
source: NeetCode 150
pattern: Tree
date: 2026-09-07
language: Python
---

## 접근법

- preorder의 첫 번째 값은 현재 서브트리의 루트이므로, `preorder_index`로 현재 루트 위치를 관리한다.
- inorder에서 각 값의 위치를 미리 저장해 루트 기준으로 왼쪽·오른쪽 서브트리 범위를 나눈다.
- 현재 루트를 만든 뒤 왼쪽 범위에 대해 재귀 호출하고, 이어서 오른쪽 범위에 대해 재귀 호출한다.
- inorder의 범위가 비어 있으면 해당 위치에는 노드가 없으므로 `None`을 반환한다.
- `preorder_index`를 재귀 호출 사이에서 유지하기 위해 `nonlocal`을 사용한다.

## 막힌 지점 또는 틀린 이유

- preorder의 루트와 inorder의 분할 규칙은 이해했지만, 이를 리스트를 직접 자르는 방식이 아닌 인덱스 범위와 재귀 함수로 옮기는 과정이 어려웠다.
- 왼쪽 서브트리의 크기를 기준으로 preorder를 직접 나누기보다, preorder의 현재 위치를 하나씩 이동시키고 inorder 범위로 재귀 대상을 제한하는 구조를 사용했다.

## 시간·공간 복잡도

- 시간 복잡도: O(n)
- 공간 복잡도: O(n), 위치 해시맵과 재귀 호출 스택

## 다음에 기억할 한 줄

- preorder로 루트를 정하고, inorder에서 그 루트의 위치를 기준으로 왼쪽·오른쪽 재귀 범위를 나눈다.
