import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())  # N: row, M: col, R: 배열 돌리기 횟수
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False for i in range(M)] for j in range(N)]
max_idx = min(N, M) // 2  # 최대로 나올 수 있는 배열 개수
arrays = [[] for _ in range(max_idx)]

for idx in range(max_idx):
    for col1 in range(idx, N-idx):
        arrays[idx].append(graph[col1][idx])
    for row1 in range(idx+1, M-idx):
        arrays[idx].append(graph[N-idx-1][row1])
    for col2 in range(N-idx-2, idx, -1):
        arrays[idx].append(graph[col2][M-idx-1])
    for row2 in range(M-idx-1, idx, -1):
        arrays[idx].append(graph[idx][row2])

# R번 회전
cir_arr = []
for arr in arrays:
    next = R % len(arr)
    tmp_arr = arr[-next:] + arr[:-next]
    cir_arr.append(tmp_arr)

# 다시 원래대로 복구
for idx in range(max_idx):
    num = 0
    for col1 in range(idx, N-idx):
        graph[col1][idx] = cir_arr[idx][num]
        num += 1 
    for row1 in range(idx+1, M-idx):
        graph[N-idx-1][row1] = cir_arr[idx][num]
        num += 1
    for col2 in range(N-idx-2, idx, -1):
        graph[col2][M-idx-1] = cir_arr[idx][num]
        num += 1
    for row2 in range(M-idx-1, idx, -1):
        graph[idx][row2] = cir_arr[idx][num]
        num += 1

for row in graph:
    print(*row, sep=" ")

