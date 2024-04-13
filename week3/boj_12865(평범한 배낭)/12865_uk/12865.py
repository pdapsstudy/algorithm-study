import sys
input = sys.stdin.readline
#어려웠던 문제.. 일차원 배열로 푸는 법도 있던데 전혀 모르겠어서 그냥 dp표를 만들고 정석적으로 풀었음
if __name__ == "__main__":                     
  #print("입력하세요")
  N, K = map(int, input().split())
  w = [0 for _ in range(101)]
  v = [0 for _ in range(101)]
  dp = [[0]*(K+1) for _ in range(N+1)] #DP N+1, K+1로 한 이유 = [i-1][j]가 존재해야하기 때문(1부터 시작해야됨)
  for i in range(1, N + 1):
      w[i], v[i] = map(int, input().split())
  for i in range(1, N+1): #고려할 물건 개수
    for j in range(1, K+1): #배낭 무게
            if j - w[i] >= 0: #현재 물건을 담을 수 있는 경우
                dp[i][j] = max(dp[i-1][j-w[i]]+v[i] , dp[i-1][j]) #dp[i-1][j] i번째 물건을 선택하지 않은 경우,  dp[i-1][j-w[i]]+v[i] i번째 물건을 선택한 경우 - i-1개의 물건 중 배낭이 버틸 수 있는 무게 j에서 i번째 물건의 무게인 w[i] 만큼을 뺏을 때 가치에다가 i번째 물건의 가치를 더한것
            else:  #현재 물건을 담을 수 있는 경우
                dp[i][j] = dp[i-1][j]
  print(dp[N][K])  