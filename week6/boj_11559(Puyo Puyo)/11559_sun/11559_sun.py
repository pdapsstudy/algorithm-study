import sys
from collections import deque

input = sys.stdin.readline
graph = [[] for _ in range(12)]

# 뿌요 정보 받기
for i in range(11, -1, -1):
    graph[i] = (list(input().rstrip()))


def print_puyo(lst):
    for i in range(11, -1, -1):
        print(*lst[i], sep="", end="\n")


# 주어진 뿌요에서 인접한 뿌요들의 위치를 bfs로 찾고 반환
def bfs(puyo):
    global graph
    global puyos
    Q = deque()
    visited = [[False for i in range(6)] for t in range(12)]

    target = graph[puyo[0]][puyo[1]]
    candidate = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    Q.append(puyo)
    visited[puyo[0]][puyo[1]] = True

    while len(Q) > 0:
        curr = Q.popleft()
        puyos.append(curr)
        for cad in candidate:
            x = curr[0] + cad[0]
            y = curr[1] + cad[1]
            if (x >= 0) and (x < 12) and (y >= 0) and (y < 6) and (graph[x][y] == target):
                if not visited[x][y]:
                    visited[x][y] = True
                    Q.append((x, y))


def find_alpha(lst):
    result = []
    for i in range(len(lst)):
        if (lst[i] != "."):
            result.append(lst[i])
    return result

# 연쇄 반응 후 중력에 의해 내려옴
def gravity():
    global graph
    flag = False  # 중력 안씀

    for i in range(6):
        col = [x[i] for x in graph]
        alpha_list = find_alpha(col)
        tmp = alpha_list + ['.' for _ in range(12-len(alpha_list))]
        if str(tmp) != str(col):  # 만일 중력 쓴 경우
            flag = True
            for t in range(12):
                graph[t][i] = tmp[t]

    return flag


cnt = 0
flag = True
is_puyo = False
while flag:
    for col in range(6):
        for row in range(12):
            if graph[row][col] != '.':
                puyos = []
                bfs((row, col))
                if (len(puyos) >= 4):
                    is_puyo = True
                    for x, y in puyos:
                        graph[x][y] = '.'
    if is_puyo:
        cnt += 1
    flag = (gravity() and is_puyo)
    is_puyo = False

print(cnt)
