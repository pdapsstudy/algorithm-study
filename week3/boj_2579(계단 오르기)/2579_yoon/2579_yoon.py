import sys

input = sys.stdin.readline

N = int(input())

# 계단의 개수 최대 300개 
stairs = [0 for _ in range(300)]

# dp테이블 초기화, 각 계단까지 도달하는 데 얻을 수 있는 최대 점수를 저장 
dp = [0 for _ in range(300)]

for i in range(N):
    stairs[i] = int(input())

# 1. 계단은 한 번에 한 계단 or 두 계단
# 2. 연속된 세 개의 계단은 x
# 3. 마지막 도착 계단은 무조건 밟기
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]   # 첫 번째 계단 + 두 번째 계단

# 세 번째 계단의 경우는 두 가지 경우의 수
dp[2] = max(stairs[0]+ stairs[2], stairs[1]+stairs[2])

# N > 3
for i in range(3, N):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[N-1])





