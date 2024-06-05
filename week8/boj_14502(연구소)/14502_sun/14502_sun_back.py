# 14502 문제 조합말고 백트래킹으로 풀기
import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    input_list = list(map(int, input().split()))
    graph.append(input_list)


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
    for i in range(N):
        cnt += graph[i].count(0)
    return cnt


max_result = 0


def set_wall(dept, graph, start):
    global max_result
    if dept == 3:
        tmp_graph = copy.deepcopy(graph)
        tmp_graph = spread(tmp_graph)
        result = count_0(tmp_graph)
        if result > max_result:
            max_result = result
        return

    for idx in range(start, N*M):
        row = idx // M 
        col = idx % M
        if graph[row][col] == 0:
            graph[row][col] = 1
            set_wall(dept+1, graph, idx)
            graph[row][col] = 0  # 다시 0으로 복귀


set_wall(0, graph, 0)
print(max_result)
