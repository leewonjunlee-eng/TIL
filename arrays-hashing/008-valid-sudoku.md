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
        values = [board[row][column] for row in range(9)]
        if not is_valid(values):
            return False

### 3. 3×3 박스 검사

박스의 시작 행과 시작 열을 각각 0, 3, 6으로 이동시킨다. 각 시작 위치에서 3칸씩 읽으면 총 9개의 3×3 박스를 확인할 수 있다.

    for row_start in range(0, 9, 3):
        for column_start in range(0, 9, 3):
            values = []

            for row in range(row_start, row_start + 3):
                for column in range(column_start, column_start + 3):
                    values.append(board[row][column])

            if not is_valid(values):
                return False

행·열·박스 어디에서도 중복이 발견되지 않으면 True를 반환한다.

## 시간·공간 복잡도

일반적인 n×n Sudoku로 생각하면:

- 시간: O(n²)
- 공간: O(n²)

이 문제의 보드는 항상 9×9로 고정되어 있으므로 실제 입력 크기 기준으로는 시간과 공간 모두 O(1)로 볼 수도 있다. 구현에서는 열과 박스를 검사할 임시 리스트와 중복 확인용 set을 사용한다.

## 막힌 지점

처음 코드에서 다음 부분을 수정했다.

- "."은 빈칸이므로 set에 넣기 전에 제외해야 한다. 빈칸 여러 개를 중복 숫자로 잘못 판단하면 안 된다.
- 열을 검사할 때는 board[row][column]처럼 행과 열의 위치를 바꿔 접근해야 한다.
- 3×3 박스는 시작 위치를 3씩 증가시키고, 각 시작 위치에서 행과 열을 각각 3칸씩 순회한다.
- 같은 중복 검사 함수에 전달하는 값만 행·열·박스로 바꾸면 코드 중복을 줄일 수 있다.

## 더 빠른 방법

현재 코드는 행, 열, 박스를 차례로 검사해서 논리 흐름을 이해하기 쉽다.

한 번의 순회로 처리하려면 rows, columns, boxes를 set 리스트로 만들고, 각 숫자를 읽을 때 동시에 세 set에 기록할 수 있다. 이 방식은 불필요한 재순회를 줄이고, 박스 번호를 (row // 3) * 3 + column // 3으로 계산한다.

다만 9×9 보드에서는 입력 크기가 고정되어 두 방식의 점근적 차이는 없고, 현재 방식이 행·열·박스를 분리해 설명하기에는 더 직관적이다.

## 다음에 기억할 한 줄

Sudoku 검사는 행·열·3×3 박스를 각각 확인하되, 빈칸을 제외한 중복 검사 로직은 함수로 재사용한다.
