N, K = map(int, input().split())
bag = [[] for _ in range(N)]  # 입력받은 [weight, value] 저장
# 열: weight (0 ~ K), 행: 입력 받은 N번 + 0으로만 이뤄진 첫행. K 무게일때의 최댓값을 의미함
graph = [[0 for _ in range(K+1)] for t in range(N+1)]


for i in range(N):
    w, v = map(int, input().split())
    bag[i] = [w, v]


def DP(weight, value, i):
    """
    weight: 현재 bag의 weight
    value: 현재 bag의 value
    i: graph 에서 i 번째 행에 해당
    """
    for t in range(1, K+1):
        # 1. 현재 물건을 넣고 남은 무게를 채울 수 있는 최댓값을 위 행에서 가져와 더함
        if t < weight:  # 물건을 넣을 수 없는 경우
            graph[i][t] = graph[i-1][t]
        # 2. 현재 물건을 넣을 수 없으면, 이전 물건들로 채우는 값을 가져옴
        else:
            graph[i][t] = max(value + graph[i-1][t - weight],
                              graph[i-1][t])


for row in range(1, N+1):
    weight, value = bag[row-1]
    DP(weight, value, row)

print(graph[N][K])
