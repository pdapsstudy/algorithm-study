from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

Q = deque()
for _ in range(N):
    command = input().strip().split(" ")
    
    if command[0] == "push":
        Q.append(command[1])

    if command[0] == "pop":
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.pop())

    if command[0] == "size":
        print(len(Q))

    if command[0] == "empty":
        if len(Q) == 0:
            print(1)
        else:
            print(0)

    if command[0] == "top":
        if len(Q) == 0:
            print(-1)
        else:
            top = Q.pop()
            print(top)
            Q.append(top)
