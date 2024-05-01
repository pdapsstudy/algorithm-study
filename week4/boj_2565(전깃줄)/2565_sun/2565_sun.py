import sys
input = sys.stdin.readline
graph = []
N = int(input())
dp = [0 for _ in range(N)]

for _ in range(N):
    line = list(map(int, input().split()))
    graph.append((line[0], line[1]))

graph.sort(key=lambda x: x[0])

# dp 초기화
for curr in range(N):
    s = graph[curr][0]
    e = graph[curr][1]
    for next in range(N):
        if (graph[next][0] > s and graph[next][1] < e) or (graph[next][0] < s and graph[next][1] > e):
            dp[curr] += 1
result = 0
while sum(dp) != 0:
    now = dp.index(max(dp))
    s = graph[now][0]
    e = graph[now][1]
    for next in range(len(dp)):
        if (graph[next][0] > s and graph[next][1] < e) or (graph[next][0] < s and graph[next][1] > e):
            dp[next] -= 1

    del graph[now]
    del dp[now]
    result += 1

print(result)