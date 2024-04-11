import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = {input().rstrip() for _ in range(N)}

for _ in range(M):
    used = set(input().rstrip().split(','))
    for i in used:
        words.discard(i)
    
    print(len(words))