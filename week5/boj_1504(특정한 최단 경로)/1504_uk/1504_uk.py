from collections import deque
import sys
input = sys.stdin.readline
#어려운 문제,, 다시 봐야할듯
#최단경로를 구하는 문제여서 bfs를 사용 c1, c2를 무조건 지나야 한다는 조건이 있기 때문에 path 하나당 세가지 1 -> c1 , c1 -> c2 , c2 -> v 이런 식으로 쪼개서 bfs 함(결국엔 다 지나가야하긴 함)
#bfs는 가는 곳이 곧 최단 경로이기 때문에 visited_len이라는 배열 따로 만들어서 새롭게 갱신된 값을 저장해주기만 하면 됨
def bfs(start, end):
    if start == end:
        return 0
    dq = deque()
    dq.append((start, 0))  
    visit_len = [-1] * (V + 1)
    visit_len[start] = 0  # 시작 정점까지의 거리는 0으로
    while dq:
        x, dist = dq.popleft()
        if x != end:  # 도착 정점에 도착했을 때 탐색 종료
          for e in MAP[x]:
            new_dist = dist + e[1]  # 현재까지의 거리에 새로운 간선의 거리를 더함
            if visit_len[e[0]] == -1 or visit_len[e[0]] > new_dist:  # 아직 방문하지 않았거나 or 최단거리 갱신
                visit_len[e[0]] = new_dist
                dq.append((e[0], new_dist))  # 도착 정점과 거리를 함께 저장
    if visit_len[end] == -1: 
         return -1
    
    return visit_len[end] 

if __name__ == "__main__":
    V, E = map(int, input().split())
    MAP = [[] for _ in range(V + 1)]
    for _ in range(E):
        start, end, dist = map(int, input().split())
        MAP[start].append((end, dist))
        MAP[end].append((start, dist))

    c1, c2 = map(int, input().split())
    path12 = [bfs(1, c1), bfs(c1, c2), bfs(c2, V)]
    path21 = [bfs(1, c2), bfs(c2, c1), bfs(c1, V)]

    if -1 in path12 and -1 in path21:
        print(-1)
    elif -1 in path12:
        print(sum(path21))
    elif -1 in path21:
        print(sum(path12))
    else:
        print(min(sum(path12), sum(path21)))