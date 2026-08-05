# TIL — NeetCode

매일 한 문제씩 풀고, 풀이 코드와 짧은 회고를 남기는 공개 학습 기록입니다.

## 기록 형식

각 문제는 패턴별 폴더에 다음 두 파일로 저장합니다.

```text
arrays-hashing/
  001-two-sum.py
  001-two-sum.md
```

회고에는 아래 네 가지만 적습니다.

1. 접근법
2. 시간·공간 복잡도
3. 막힌 지점 또는 틀린 이유
4. 다음에 기억할 한 줄

## 원칙

- Python으로 풉니다.
- 하루 한 문제를 목표로 하되, 억지 커밋보다 이해한 내용을 남깁니다.
- 제출 코드와 회고는 직접 작성합니다.


## Codespace and SSH setup
매일 문제 하나씩
ssh -i /workspaces/TIL/Second_Brain.key ubuntu@134.185.105.21
ssh -i /workspaces/TIL/Second_Brain.key -v ubuntu@134.185.105.21
ssh -i /workspaces/TIL/Second_Brain.key -L 9119:127.0.0.1:9119 -L 3000:127.0.0.1:3000 ubuntu@134.185.105.21
ssh -i /workspaces/TIL/Second_Brain.key -L 3000:127.0.0.1:3000 ubuntu@134.185.105.21



http://127.0.0.1:9119/
http://127.0.0.1:3000/


{
    "sshfs.configs": [
        
        {
            "name": "oracle-second-brain",
            "host": "134.185.105.21",
            "port": 22,
            "type": "ssh",
            "username": "ubuntu",
            "privateKeyPath": "/workspaces/TIL/Second_Brain.key"
        }
    ]
}