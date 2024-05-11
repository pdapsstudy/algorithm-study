import sys
from collections import deque
input = sys.stdin.readline


def main():
    gongsan = list(input().rstrip())
    cursor = 0  # 커서 위치
    Q = deque()
    for i in range(len(gongsan)):
        if gongsan[i] == ">":
            if cursor != len(Q):  # 커서 뒤로
                cursor += 1
        elif gongsan[i] == "<":  # 커서 앞으로
            if cursor != 0:
                cursor -= 1
        elif gongsan[i] == "-":  # 현재 커서 위치에서 하나 삭제
            if cursor != 0:
                del Q[cursor-1]
                cursor -= 1
        else:
            Q.insert(cursor, gongsan[i])
            cursor += 1
    password = ""
    while len(Q) > 0:
        password += Q.popleft()
    return password


L = int(input())
for _ in range(L):
    print(main())
