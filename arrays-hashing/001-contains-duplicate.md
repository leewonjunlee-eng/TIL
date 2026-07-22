---
title: Contains Duplicate
source: NeetCode 150
pattern: Arrays & Hashing
date: 2026-07-20
language: Python
---




# Contains Duplicate




## 접근법




처음에는 `result` 리스트에 이미 본 숫자를 저장했다.




```python
if num in result:
```




하지만 리스트 포함 여부 확인은 숫자가 늘수록 앞에서부터 더 많이 찾아야 한다. 중복 여부만 확인하면 되므로, `set`으로 바꿨다.




```python
seen = set()




for num in nums:
    if num in seen:
        return True
    seen.add(num)




return False
```




## 시간·공간 복잡도




- 시간: `O(n)`
- 공간: `O(n)`
