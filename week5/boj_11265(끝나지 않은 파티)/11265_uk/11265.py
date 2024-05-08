import sys
input = sys.stdin.readline

if __name__ == "__main__":
    # N = map(int, input().split())
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
   

    #경유해서 더 빠른거
    for k in range(N):
      for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
               graph[i][j] = graph[i][k] + graph[k][j]

    for i in range(M):
        s, d, t = map(int, input().split())
        if graph[s-1][d-1] <= t:
            print("Enjoy other party")
        else:
            print("Stay here")
