import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = set()
for _ in range(N):
    word = input().rstrip()
    words.add(word)

for _ in range(M):
    used = set(input().rstrip().split(','))
    for i in used:
        words.discard(i)
    
    print(len(words))