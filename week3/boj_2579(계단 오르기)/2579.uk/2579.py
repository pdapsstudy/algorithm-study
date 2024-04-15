#계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
#연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
#마지막 도착 계단은 반드시 밟아야 한다.

#계단을 밟는 경우(1번 연속, 2번 연속) 과 밟지 않은 경우(이전에 밟았을 때만 선택)
#dp[i][j] = i번 계단을 j번 연속 밟을 때 최대점수
import sys
input = sys.stdin.readline

if __name__ == "__main__":                     
  #print("입력하세요")
  N = int(input())
  stair = [0] + [int(input()) for _ in range(N)]
  dp = [[0]*3 for _ in range(N+1)]
  
  for i in range(1, N+1):
     dp[i][0] = max(dp[i-1][1], dp[i-1][2]) # 안 밟는 경우
     dp[i][1] = dp[i-1][0] + stair[i]  # 1번 연속 밟는 경우
     dp[i][2] = dp[i-1][1] + stair[i]  # 2번 연속 밟는 경우


  print(max(dp[N][1], dp[N][2]))