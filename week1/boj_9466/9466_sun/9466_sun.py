import sys

input = sys.stdin.readline
M = int(input())

def search(target, now):
    global visited
    if now == target:
        visited[now] = True
        return True
    
    next = graph[now]
    if not visited[next]:
        visited[next] = True
        flag = search(target, next)
        # 만일 친구 순환 만들어지지 않은 경우 -> 백트래킹으로 방문 해제
        if not flag:
            visited[next] = False
    else:
        return False
        
    
for _ in range(M):
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    count = 0

    for node in range(1, N):
        if not visited[node]:
            flag = search(node, graph[node])
            print(f"node {node} flag {flag}")
            print(f"visited {visited}")
            if flag:
                count += 1
    print(count)
            

