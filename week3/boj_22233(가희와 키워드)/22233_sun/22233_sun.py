import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = {}
count = N

for _ in range(N):
    words[input().replace('\n', '')] = 1


for _ in range(M):
    input_list = list(input().replace('\n', '').split(','))
    for i in input_list:
        if i in words.keys():
            if words[i] == 1:
                words[i] = 0
                count -= 1
    print(count)
