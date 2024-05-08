#########################################################
# 처음 시도한 방법: 많이 꼬인 전기줄부터 제거하자
# 안먹히는 반례가 생김: https://www.acmicpc.net/board/view/84972 참고
# dp 로 해결해야함 -> 생각 너무 안나서 블로그 참고

import sys
input = sys.stdin.readline
graph = []
N = int(input())
dp = [1 for _ in range(N)]

for _ in range(N):
    line = list(map(int, input().split()))
    graph.append((line[0], line[1]))

graph.sort(key=lambda x: x[0])

for i in range(N):
    for j in range(i):
        if graph[i][1] > graph[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))