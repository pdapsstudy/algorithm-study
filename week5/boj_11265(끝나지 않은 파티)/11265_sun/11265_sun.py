import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)]]

for _ in range(N):
    tt = [0] + list(map(int, input().split()))
    graph.append(tt)

## 플로이드 워셜 알고리즘 사용해봄 (블로그 참고)
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if a==b: 
                continue
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
for i in range(M):
    s, e, t = map(int, input().split())
    if graph[s][e] <= t:
        print("Enjoy other party")
    else:
        print("Stay here")

