# 이게 왜 이진탐색인지 잘..그리디로 푸는줄 알았음
# 어떤 값으로 비교할지 선택만 잘하면 됨 여기서는 mid(시간)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

if __name__ == "__main__":
    #print("입력하세요") 
    N, person = map(int, input().split())
    arr = []
    
    for _ in range(N):
        arr.append(int(input()))
 
    #print(arr)
    start = 1
    end = max(arr) * person # 최대로 줄 수 있는 시간
    ans = max(arr) * person
    while start <= end:
       mid = (start + end) // 2  # mid = 시간
       sum = 0
       for i in range(N):
           sum += (mid // arr[i])
       if sum >= person:
           end = mid - 1
           ans = min(ans, mid)
       
       else:
           start = mid + 1    
    print(ans)