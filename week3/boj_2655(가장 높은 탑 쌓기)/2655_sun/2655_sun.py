N = int(input())
bricks = [[0 for i in range(4)] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
path = []

for i in range(1, N+1):
    floor, height, weight = map(int, input().split())
    bricks[i] = [i, floor, height, weight] # i(0): 벽돌 번호, floor(1): 밑면의 넓이, height(2): 높이, weight(3): 무게

# 무게를 기준으로 오름차순 정렬
bricks.sort(key=lambda x: (x[-1]))


# idx 번째 brick이 가장 바닥일 때 가정
for idx in range(1, N+1):
    # next: idx brick 위에 올릴 수 있는 벽돌 (무게가 더 작은 벽돌)
    for next in range(idx):
        if bricks[next][1] < bricks[idx][1]:
            dp[idx] = max(dp[idx], dp[next]+bricks[idx][2])

max_brick = max(dp)
# print(dp)
# print(bricks)
index = N

# 역으로 index를 바탕으로 왔던 길 찾기
while index !=0:
    if max_brick == dp[index]:
        path.append(bricks[index][0])
        max_brick -= bricks[index][2]
    index -= 1

print(len(path))
for i in range(len(path)-1, -1, -1):
    print(path[i])