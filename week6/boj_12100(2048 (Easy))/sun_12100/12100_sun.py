import sys
import copy
input = sys.stdin.readline

N = int(input())

input_graph = []
for _ in range(N):
    input_graph.append(list(map(int, input().split()))+[0])


def move(graph, direction):
    if direction == "Up":
        tmp_graph = list(map(list, zip(*graph)))
        for row in range(N):
            tmp = []
            before = tmp_graph[row][0]
            flag = False
            for col in range(1, N):
                if tmp_graph[row][col] == 0:
                    continue
                elif before == 0:
                    before = tmp_graph[row][col]
                    flag = False
                elif before == tmp_graph[row][col]:
                    tmp.append(before*2)
                    flag = True
                    before = 0
                elif before != tmp_graph[row][col]:
                    tmp.append(before)
                    before = tmp_graph[row][col]
                    flag = False
            if not flag:
                tmp.append(before)
            tmp_graph[row] = tmp + [0 for _ in range(N-len(tmp))]

        graph = list(map(list, zip(*tmp_graph)))

    if direction == "Down":
        tmp_graph = list(map(list, zip(*graph)))
        for row in range(N):
            tmp = []
            before = tmp_graph[row][N-1]
            flag = False
            for col in range(N-2, -1, -1):
                if tmp_graph[row][col] == 0:
                    continue
                elif before == 0:
                    before = tmp_graph[row][col]
                    flag = False
                elif before == tmp_graph[row][col]:
                    tmp.insert(0, before*2)
                    flag = True
                    before = 0
                elif before != tmp_graph[row][col]:
                    tmp.insert(0, before)
                    before = tmp_graph[row][col]
                    flag = False
            if not flag:
                tmp.insert(0, before)
            tmp_graph[row] = [0 for _ in range(N-len(tmp))] + tmp
        graph = list(map(list, zip(*tmp_graph)))

    if direction == "Right":
        for row in range(N):
            tmp = []
            before = graph[row][N-1]
            flag = False  # 마지막 요소 들어갔는지 확인
            for col in range(N-2, -1, -1):
                if graph[row][col] == 0:
                    continue
                elif before == 0:
                    before = graph[row][col]
                    flag = False
                elif before == graph[row][col]:
                    tmp.insert(0, before*2)
                    flag = True
                    before = 0
                elif before != graph[row][col]:
                    tmp.insert(0, before)
                    before = graph[row][col]
                    flag = False
            if not flag:
                tmp.insert(0, before)
            graph[row] = [0 for _ in range(N-len(tmp))] + tmp

    if direction == "Left":
        for row in range(N):
            tmp = []
            before = graph[row][0]
            flag = False
            for col in range(1, N):
                if graph[row][col] == 0:
                    continue
                elif before == 0:
                    before = graph[row][col]
                    flag = False
                elif before == graph[row][col]:
                    tmp.append(before*2)
                    flag = True
                    before = 0
                elif before != graph[row][col]:
                    tmp.append(before)
                    before = graph[row][col]
                    flag = False
            if not flag:
                tmp.append(before)
            graph[row] = tmp + [0 for _ in range(N-len(tmp))]

    return graph


def process(graph):
    final = []
    for direct1 in ["Up", "Down", "Right", "Left"]:
        graph1 = copy.deepcopy(graph)
        graph2 = move(graph1, direct1)
        for direct2 in ["Up", "Down", "Right", "Left"]:
            graph3 = copy.deepcopy(graph2)
            graph4 = move(graph3, direct2)
            for direct3 in ["Up", "Down", "Right", "Left"]:
                graph5 = copy.deepcopy(graph4)
                graph6 = move(graph5, direct3)
                for direct4 in ["Up", "Down", "Right", "Left"]:
                    graph7 = copy.deepcopy(graph6)
                    graph8 = move(graph7, direct4)
                    for direct5 in ["Up", "Down", "Right", "Left"]:
                        graph9 = copy.deepcopy(graph8)
                        graph10 = move(graph9, direct5)
                        y = list(map(max, graph10))
                        final.append(max(y))
    return max(final)

print(process(input_graph))
