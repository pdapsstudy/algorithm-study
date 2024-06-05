import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    input_list = list(map(int, input().split()))
    graph.append(input_list)

blank = []
for row in range(N):
    for col in range(M):
        if graph[row][col] == 0:
            blank.append((row, col))


def spread(graph):
    visited = [[False for _ in range(M)] for i in range(N)]
    Q = deque()

    # 만약 전염병에 감염된 칸 넣기
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 2:
                visited[row][col] = True
                Q.append((row, col))

    while len(Q) > 0:
        row, col = Q.popleft()
        visited[row][col] = True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = row + dx
            y = col + dy
            if x >= 0 and x < N and y >= 0 and y < M:
                if visited[x][y] == False and graph[x][y] != 1:
                    graph[x][y] = 2
                    Q.append((x, y))
                    visited[x][y] = True

    return graph


def count_0(graph):
    cnt = 0
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 0:
                cnt += 1
    return cnt


max_result = 0
for l in combinations(blank, 3):
    tmp_graph = copy.deepcopy(graph)
    for x, y in l:
        tmp_graph[x][y] = 1

    tmp_graph = spread(tmp_graph)
    result = count_0(tmp_graph)
    if result > max_result:
        max_result = result

print(max_result)
