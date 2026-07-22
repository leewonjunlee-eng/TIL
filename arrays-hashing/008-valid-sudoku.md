---
title: Valid Sudoku
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-22
language: Python
---


# Valid Sudoku


## 접근법


Sudoku가 유효하려면 같은 숫자가 다음 세 영역에서 반복되면 안 된다.


- 각 행
- 각 열
- 각 3×3 박스


행·열·박스에서 사용하는 중복 검사 로직은 is_valid() 함수로 분리했다. 빈칸을 나타내는 "."은 검사에서 제외한 뒤, 리스트의 길이와 set의 길이를 비교한다.


    def is_valid(values: List[str]) -> bool:
        values = [value for value in values if value != "."]
        return len(values) == len(set(values))


### 1. 행 검사


board의 각 행을 그대로 함수에 전달한다.


    for row in board:
        if not is_valid(row):
            return False


### 2. 열 검사


열 번호를 0부터 8까지 순회하면서 해당 열의 값을 새 리스트로 만든다.


    for column in range(9):
