import sys
from queue import PriorityQueue
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])

V1, V2 = map(int, input().split())

for i in range(len(graph)):
    graph[i].sort(key=lambda x: x[1])

def dijkstra(start, end):
    global graph
    distance = [sys.maxsize] * (N+1)
    visited = [False] * (N+1)
    PQ = PriorityQueue()
    distance[start] = 0
    PQ.put((0, start))  # start를 시작점으로 설정

    while PQ.qsize() > 0:
        current = PQ.get()
        if visited[current[1]]: # 만일 이미 방문한 노드라면, 
            continue
        visited[current[1]] = True

        for tt in graph[current[1]]:
            next = tt[0]
            weight = tt[1]
            if distance[next] > distance[current[1]] + weight:
                distance[next] = distance[current[1]] + weight
                PQ.put((distance[next], next))

    return distance[end]


# start ~ V1 까지 거리, start ~ V2 까지 거리
D1 = dijkstra(1, V1)
D2 = dijkstra(1, V2)

# V1 ~ V2 거리
T1 = dijkstra(V1, V2)

# V1 ~ end 까지 거리, V2 ~ end 까지 거리
M1 = dijkstra(V1, N)
M2 = dijkstra(V2, N)

# print(f"D1 {D1} D2 {D2} T1 {T1} M1 {M1} M2 {M2}")
dist = min(D1+M2, D2+M1) + T1

if dist >= sys.maxsize:
    print(-1)
else:
    print(dist)
