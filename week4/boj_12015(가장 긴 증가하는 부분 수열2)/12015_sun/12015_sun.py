import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

sorted_arr = [(arr[i], i) for i in range(N)] # (arr 요소, index)로 리스트에 저장함
sorted_arr.sort(key = lambda x :(x[0], x[1])) # 오름차순으로 정렬
dp = [1 for _ in range(N)] # 올릴 수 있는 벽돌 개수 append 

for curr in range(1, N): # 현재 벽돌이 가장 바닥에 깔릴때, 위로 올릴 수 있는 벽돌 counting
    for next in range(curr):
        if sorted_arr[curr][0] > sorted_arr[next][0] and sorted_arr[curr][1] > sorted_arr[next][1]:
            dp[curr] = max(dp[curr], dp[next]+1)    

print(max(dp))

