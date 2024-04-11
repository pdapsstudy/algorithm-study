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
        words.discard(i)    # remove()로 하면 오류 체크 필요..
    
    print(len(words))

# 런타임 에러 코드
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# words = []

# for _ in range(N):
#     word = input().rstrip()
#     words.append(word)

# for _ in range(M):
#     a, b = input().rstrip().split(',')
#     if a in words:
#         words.remove(a)
#     if b in words:
#         words.remove(b)
#     print(len(words))
    