import sys
input = sys.stdin.readline
N = int(input())
total_num = N*N
fav_friend = {}
graph = [[0 for i in range(N)] for t in range(N)]

for _ in range(total_num):
    input_list = list(map(int, input().split()))
    fav_friend[input_list[0]] = input_list[1:]


def set_priority(row, col, friend):
    global graph

    dt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    empty_cnt = 0
    friend_cnt = 0  # 인접한 친구 개수
    for dx, dy in dt:
        x = dx + row
        y = dy + col
        # 범위 안에
        if x >= 0 and x < N and y >= 0 and y < N:
            if graph[x][y] in friend:
                friend_cnt += 1
            elif graph[x][y] == 0:
                empty_cnt += 1
    return friend_cnt, empty_cnt


target = {key: value[0] for key, value in fav_friend.items()}
targets = list(fav_friend.keys())
idx = 0
while idx < total_num:
    target = targets[idx]
    candidate = []
    for row in range(N):
        for col in range(N):
            # 그래프의 우선 순위 따지기
            if graph[row][col] == 0:
                f_priority, e_priority = set_priority(
                    row, col, fav_friend[target])
                candidate.append([f_priority, e_priority, row, col])

    candidate.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # 들어갈 자리 정하기
    place = (candidate[0][2], candidate[0][3])

    # 자리 넣고 + 다음 친구 차례~
    graph[place[0]][place[1]] = target
    idx += 1

happiness = 0
for row in range(N):
    for col in range(N):
        target = graph[row][col]
        friends = fav_friend[target]
        dt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        friend_cnt = 0
        for dx, dy in dt:
            x = dx + row
            y = dy + col
            if x >= 0 and x < N and y >= 0 and y < N:
                if graph[x][y] in friends:
                    friend_cnt +=1
        if friend_cnt == 1:
            happiness += 1
        if friend_cnt == 2:
            happiness += 10
        if friend_cnt == 3:
            happiness += 100
        if friend_cnt == 4:
            happiness += 1000

print(happiness)