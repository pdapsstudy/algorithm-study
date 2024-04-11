import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = set()   # 리스트 쓰면 제대로 안 지워져 왜지..?
for _ in range(N):
    word = input().rstrip()
    words.add(word)

for _ in range(M):
    used = set(input().rstrip().split(','))
    for i in used:
        words.discard(i)    # remove()로 하면 오류 체크 필요,,
    
    print(len(words))