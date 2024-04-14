N = int(input())
stair = [0]
dp = [0] * (N+1)

for _ in range(N):
    stair.append(int(input()))

if N < 2: # 만일 주어진 계단의 개수가 2보다 적은 경우
    print(stair[N]) 

else:
    dp[1] = stair[1]
    dp[2] = dp[1] + stair[2]
    for i in range(3, N+1):
        # i-3, i-1 계단 밟기 or i-2 계단 밟기
        dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]
    print(dp[N])
    
